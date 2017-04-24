from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from polls.models import Notes, Choices


class BirthdayVoteForm(ModelForm):
    class Meta:
        model = Choices
        widgets = {'choice_fields': forms.RadioSelect()}
        fields = ('choice_fields',)


class BirthdayNoteForm(ModelForm):
    class Meta:
        model = Notes
        fields = ('notes_field',)


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")
        field_classes = {'username': UsernameField}


