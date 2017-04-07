from django.conf.urls import url
from . import views


app_name = 'polls'

urlpatterns = [
    url(r'^login/$', views.get_login, name='login'),
    url(r'^registration/$', views.get_registration, name='create_user'),
    url(r'^voting/$', views.get_voting, name='voting'),
    url(r'^notes/$', views.get_notes, name='notes'),
    url(r'^thank_you/$', views.get_thank_you_page, name='thank_you')
]

