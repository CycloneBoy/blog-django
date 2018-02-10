from django.conf.urls import url
from . import views

app_name = 'account'


urlpatterns = [
    # /login/
    url(r'^login/$', views.user_login, name='user_login'),

]
