from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'p_site.views.articles', name='articles'),

    url(r'^articles/get/(?P<article_id>\d+)/$', 'p_site.views.article', name='article'),
    url(r'^articles/addlike/(?P<article_id>\d+)/$', 'p_site.views.addlike', name='addlike'),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', 'p_site.views.addcomment', name='addcomment'),

    url(r'^page/(\d+)/$', 'p_site.views.articles', name='articles'),
    url(r'^category/get/(?P<category_id>\d+)/$', 'p_site.views.article_cat', name='article_cat'),
    url(r'^keyword/$', 'p_site.views.keywords', name='keywords'),
    url(r'^author/(?P<id>\d+)/$', 'p_site.views.authors', name='authors'),
    url(r'^home/$', 'p_site.views.home', name='home'),
    ]