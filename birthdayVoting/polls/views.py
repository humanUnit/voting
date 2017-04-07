from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import BirthdayVoteForm, BirthdayNoteForm, AuthenticationForm, RegistrationForm


def get_voting(request):
    if request.method == 'POST':
        form = BirthdayVoteForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/notes/')
    else:
        form = BirthdayVoteForm()
    return render(request, 'voting_form.html', {'form': form})


def get_notes(request):
    if request.method == 'POST':
        form = BirthdayNoteForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/thank_you/')

    else:
        form = BirthdayNoteForm()
    return render(request, 'notes_form.html', {'form': form})


def get_thank_you_page(request):
    if request.method == 'POST':
        return HttpResponseRedirect('')
    return render(request, 'thank_you_page.html')


def get_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/registration/')

    else:
        form = AuthenticationForm()
    return render(request, 'login_form.html', {'form': form})


def get_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/voting/')

    else:
        form = RegistrationForm()
    return render(request, 'registration_form.html', {'form': form})
