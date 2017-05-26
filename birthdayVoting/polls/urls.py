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

    url(r'^thank_you/$', views.get_thank_you_page, name='thank_you')
]
