# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField
from embed_video.fields import EmbedVideoField
import mptt
from mptt.models import MPTTModel, TreeForeignKey

class Home(models.Model):
    class Meta():
        db_table = 'home'
        verbose_name_plural = 'Статичные страницы'
        verbose_name = 'Главная страница'
    home_title = models.CharField(null=True, blank=True, max_length=200)
    home_text = HTMLField(null=True, blank=True)
    home_date = models.DateField(null=True, blank=True)
    home_image = models.ImageField(null=True, blank=True, upload_to='image/', verbose_name=u'Изображение')
    video = EmbedVideoField(null=True, blank=True, verbose_name=u'Видео')

    def __unicode__(self):
        return self.home_title

    def bit_home(self):
        if self.home_image:
            return u'<img src="%s" width="70"/>' % self.home_image.url
        else:
            return u'(none)'
    bit_home.short_descriptio = u'Изображение'
    bit_home.allow_tags = True


class Keywords(models.Model):
    class Meta():
        db_table = 'keywords'
        verbose_name_plural = 'Теги'
        verbose_name = 'Теги'

    name = models.CharField(max_length=50, unique=True, verbose_name=u'Поиск по сайту:')

    def __unicode__(self):
        return self.name


class Author(models.Model):
    class Meta():
        db_table = 'author'
        verbose_name_plural = 'Авторы'
        verbose_name = 'Автор'

    name = models.CharField(max_length=150)
    author_image = models.ImageField(null=True, blank=True, upload_to="img/", verbose_name="Фото автора",  help_text="250x25")

    def __unicode__(self):
        return self.name

    def bit_author(self):
        if self.author_image:
            return u'<img src="%s" width="70"/>' % self.author_image.url
        else:
            return u'(none)'
    bit_author.short_descriptio = u'Изображение'
    bit_author.allow_tags = True


class Category(MPTTModel):
    class Meta():
        db_table = 'category'
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ('tree_id', 'level')

    name = models.CharField(max_length=150, verbose_name = 'Категория')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name=u'РОДИТЕЛЬСКИЙ класс')

    def __unicode__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

mptt.register(Category, order_insertion_by=['name'])


class Article(models.Model):
    class Meta():
        ordering = ['-article_date']
        db_table = 'article'
        verbose_name_plural = 'Статьи'
        verbose_name = 'Статьи'

    article_title = models.CharField(max_length=200, verbose_name=u'Статьи')
    article_img = models.ImageField(null=True, blank=True, upload_to="img/", verbose_name='Изображения',  help_text="150x150")
    article_video = EmbedVideoField(null=True, blank=True, verbose_name=u'Видео')
    article_text = HTMLField(null=True, blank=True)
    article_text_min = HTMLField(null=True, blank=True, max_length=600, verbose_name='Аннотация к статье')
    article_date = models.DateTimeField()
    author = models.ForeignKey(Author, max_length=150, verbose_name='Имя автор')
    article_like = models.IntegerField(default=0)
    category = TreeForeignKey(Category, blank=True, null=True, related_name='cat')
    keywords = models.ManyToManyField(Keywords, related_name='keywords', related_query_name='keyword', verbose_name=u'Теги')

    def __unicode__(self):
        return self.article_title

    def __str__(self):
        return self.article_title

    def bit(self):
        if self.article_img:
            return u'<img src="%s" width="70"/>' % self.article_img.url
        else:
            return '(none)'
    bit.short_description = u'Изображение'
    bit.allow_tags = True



class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    comments_text = models.TextField(null=True, blank=True, verbose_name='Текст коментария')
    comments_article = models.ForeignKey(Article)
    comments_date = models.DateField(u'date', auto_now=True)
    comments_author = models.ForeignKey(User)