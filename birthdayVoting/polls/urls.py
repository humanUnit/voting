from django.conf.urls import url
from . import views


app_name = 'polls'

urlpatterns = [
    url(r'^voting/$', views.get_voting, name='name'),
    url(r'^notes/$', views.get_notes, name='notes'),
    url(r'^thank_you/$', views.get_thank_you_page, name='thank_you')
]

