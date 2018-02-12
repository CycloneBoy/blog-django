from django.conf.urls import url
from . import views


app_name = 'article'


urlpatterns = [
    # /article-column/
    url(r'^article-column/$', views.article_column, name='article_column'),

]
