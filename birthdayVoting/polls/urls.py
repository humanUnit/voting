from django.conf.urls import url
from . import views


app_name = 'polls'

urlpatterns = [
    url(r'^voting/$', views.get_name, name='name'),
    url(r'^notes/$', views.get_something, name='notes'),
]

