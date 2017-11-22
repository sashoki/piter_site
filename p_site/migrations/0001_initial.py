# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-13 12:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields
import mptt.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200, verbose_name='\u0421\u0442\u0430\u0442\u044c\u0438')),
                ('article_img', models.ImageField(blank=True, help_text='150x150', null=True, upload_to='img/', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f')),
                ('article_video', embed_video.fields.EmbedVideoField(blank=True, null=True, verbose_name='\u0412\u0438\u0434\u0435\u043e')),
                ('article_text', tinymce.models.HTMLField(blank=True, null=True)),
                ('article_text_min', tinymce.models.HTMLField(blank=True, max_length=300, null=True, verbose_name='\u0410\u043d\u043d\u043e\u0442\u0430\u0446\u0438\u044f \u043a \u0441\u0442\u0430\u0442\u044c\u0435')),
                ('article_date', models.DateTimeField()),
                ('article_like', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-article_date'],
                'db_table': 'article',
                'verbose_name': '\u0421\u0442\u0430\u0442\u044c\u0438',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u044c\u0438',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('author_image', models.ImageField(blank=True, help_text='250x25', null=True, upload_to='img/', verbose_name='\u0424\u043e\u0442\u043e \u0430\u0432\u0442\u043e\u0440\u0430')),
            ],
            options={
                'db_table': 'author',
                'verbose_name': '\u0410\u0432\u0442\u043e\u0440',
                'verbose_name_plural': '\u0410\u0432\u0442\u043e\u0440\u044b',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='p_site.Category', verbose_name='\u0420\u041e\u0414\u0418\u0422\u0415\u041b\u042c\u0421\u041a\u0418\u0419 \u043a\u043b\u0430\u0441\u0441')),
            ],
            options={
                'ordering': ('tree_id', 'level'),
                'db_table': 'category',
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments_text', models.TextField(blank=True, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a\u043e\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u044f')),
                ('comments_date', models.DateField(auto_now=True, verbose_name='date')),
                ('comments_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_site.Article')),
                ('comments_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_title', models.CharField(blank=True, max_length=200, null=True)),
                ('home_text', tinymce.models.HTMLField(blank=True, null=True)),
                ('home_date', models.DateField(blank=True, null=True)),
                ('home_image', models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('video', embed_video.fields.EmbedVideoField(blank=True, null=True, verbose_name='\u0412\u0438\u0434\u0435\u043e')),
            ],
            options={
                'db_table': 'home',
                'verbose_name': '\u0413\u043b\u0430\u0432\u043d\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u0438\u0447\u043d\u044b\u0435 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
            },
        ),
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0441\u0430\u0439\u0442\u0443:')),
            ],
            options={
                'db_table': 'keywords',
                'verbose_name': '\u0422\u0435\u0433\u0438',
                'verbose_name_plural': '\u0422\u0435\u0433\u0438',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(max_length=150, on_delete=django.db.models.deletion.CASCADE, to='p_site.Author', verbose_name='\u0418\u043c\u044f \u0430\u0432\u0442\u043e\u0440'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='p_site.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='keywords',
            field=models.ManyToManyField(related_name='keywords', related_query_name='keyword', to='p_site.Keywords', verbose_name='\u0422\u0435\u0433\u0438'),
        ),
    ]
