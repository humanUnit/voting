from django.forms import ModelForm
from django import forms
from polls.models import Notes, Choices, Login, CreateAccount


class BirthdayVoteForm(ModelForm):
    class Meta:
        model = Choices
        widgets = {'choice_fields': forms.RadioSelect()}
        fields = ('choice_fields',)


class BirthdayNoteForm(ModelForm):
    class Meta:
        model = Notes
        fields = ('notes_field',)


class AuthenticationForm(ModelForm):
    class Meta:
        model = Login
        fields = ('email_address', 'password')
        widgets = {'remember_me_on_this_computer': forms.CheckboxInput()}


class RegistrationForm(ModelForm):
    class Meta:
        model = CreateAccount
        fields = ('name', 'surname', 'email_address', 'password', 'confirm_password')


