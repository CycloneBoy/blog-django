from django.conf.urls import url
from . import views

from django.contrib.auth import views as auth_views

app_name = 'account'


urlpatterns = [
    # /login/
    #url(r'^login/$', views.user_login, name='user_login'),
    url(r'^login/$', auth_views.login, name='user_login'),
    url(r'^new-login/$', auth_views.login, {"template_name": "account/login.html"}),

    # /logout/
    #url(r'^logout/$', auth_views.logout, name='user_logout'),
    url(r'^logout/$', auth_views.logout, {"template_name": "account/logout.html"},
        name='user_logout'),

    # /register/
    url(r'^register/$', views.register, name='user_register'),

    # /password-change/
    url(r'^password-change/$', auth_views.password_change,
        {"template_name": "account/password_change_form.html",
         "post_change_redirect": "/account/password-change-done"}, name="password_change",
        ),
    url(r'^password-change-done/$', auth_views.password_change_done,
        {"template_name": "account/password_change_done.html"},
        name="password_change_done"),

    # /password-change
    url(r'^password-reset/$', auth_views.password_reset,
        {"template_name": "account/password_reset_form.html",
         "email_template_name": "account/password_reset_email.html",
         "subject_template_name": "account/password_reset_subject.txt",
         "post_reset_redirect": "/account/password-reset-done"},
        name="password_reset"),
    url(r'^password-reset-done/$', auth_views.password_reset_done,
        {"template_name": "account/password_reset_done.html"},
        name="password_reset_done"),
    url(r'^password-reset-confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        auth_views.password_reset_confirm,
        {"template_name": "account/password_reset_confirm.html"},
        name="password_reset_confirm"),
    url(r'^password-reset-complete/$', auth_views.password_reset_complete,
        {"template_name": "account/password_reset_complete.html"},
        name="password_reset_complete"),

    # /send-email/
    url(r'^send-email/$', views.send_email_test, name='send_email_test'),

    # /my-information/
    url(r'^my-information/$', views.myself, name='my_information'),

    # /edit-my-information/
    url(r'^edit-my-information/$', views.myself_edit, name='edit_my_information'),

    # /my-image/
    url(r'^my-image/$', views.my_image, name='my_image'),

    # /my-image/
    url(r'^my-image-test/$', views.my_image_test, name='my_image_test'),
]
