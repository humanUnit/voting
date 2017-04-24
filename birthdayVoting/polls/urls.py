from django.conf.urls import url
from polls.forms import UserRegistrationForm
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView

app_name = 'polls'

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    url(r'^register/', CreateView.as_view(
            template_name='registration/register.html',
            form_class=UserRegistrationForm,
            success_url="/polls/login/"
    ), name='register'),

    url(r'^voting/$', views.get_voting, name='voting'),
    url(r'^notes/$', views.get_notes, name='notes'),
    url(r'^thank_you/$', views.get_thank_you_page, name='thank_you')
]
