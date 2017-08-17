from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'polls'

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    url(r'^register/', views.get_register, name='register'),

    url(r'^voting/$', views.get_voting, name='voting'),
    url(r'^choice_made/$', views.get_choices, name='choice_made'),

    url(r'^notes/$', views.get_notes, name='notes'),
    url(r'^notes_made/$', views.get_note, name='notes_made'),

    url(r'^thank_you/$', views.get_thank_you_page, name='thank_you'),

    url(r'^profile/$', views.update_profile, name='profile'),

    url(r'^admin/$', views.get_admin, name='admin'),

    url(r'^delete_user/(?P<user_id>\d+)/$', views.delete_user, name='delete_user'),

    url(r'^delete_choice/$', views.delete_choice, name='delete_choice'),

    url(r'^delete_notes/(?P<notes_id>\d+)/$', views.delete_notes, name='delete_notes'),

    url(r'^settings/$', views.get_settings, name='settings'),

    url(r'^create_notes/$', views.create_notes_field, name='create_notes'),

    url(r'^delete_notes_field/(?P<notes_id>\d+)/$', views.delete_notes_field, name='delete_notes_field'),

    url(r'^change_password/$', views.change_password, name='change_password'),

]
