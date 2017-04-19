from django.conf.urls import include, url
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^password_reset/$',
        auth_views.PasswordResetView.as_view(email_template_name='registration/password_reset_email.html')),
    url('^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url('^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]
