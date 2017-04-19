from django.forms import ModelForm
from django import forms
from polls.models import Notes, Choices, User


class BirthdayVoteForm(ModelForm):
    class Meta:
        model = Choices
        widgets = {'choice_fields': forms.RadioSelect()}
        fields = ('choice_fields',)


class BirthdayNoteForm(ModelForm):
    class Meta:
        model = Notes
        fields = ('notes_field',)


class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {'password': forms.PasswordInput()}


