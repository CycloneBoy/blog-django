from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    # /blog/
    url(r'^$', views.blog_title, name='blog_title'),

    # /blog/<article_id>/
    url(r'^(?P<article_id>[0-9]+)/$', views.blog_articles, name='blog_detail'),

]
