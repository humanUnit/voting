from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

app_name = 'polls'

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    url(r'^logout/$', views.logout, name='logout'),

    url('^register/', CreateView.as_view(
            template_name='registration/register.html',
            form_class=UserCreationForm,
            success_url='/'
    )),

    url(r'^voting/$', views.get_voting, name='voting'),
    url(r'^notes/$', views.get_notes, name='notes'),
    url(r'^thank_you/$', views.get_thank_you_page, name='thank_you')
]
