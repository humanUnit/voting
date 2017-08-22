from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from .models import Notes, Choices, Profile, ChoicesCreate


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
        fields = ("username", "email",)
        field_classes = {'username': UsernameField}


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", 'email',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birth_date',)
        widgets = {'birth_date': forms.SelectDateWidget(years=range(1970, 2010))}


class CreateChoiceForm(forms.ModelForm):
    class Meta:
        model = ChoicesCreate
        widgets = {'choice_field': forms.RadioSelect()}
        fields = ('choice_field',)