from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import BirthdayVoteForm, BirthdayNoteForm


def get_name(request):

    if request.method == 'POST':
        form = BirthdayVoteForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/notes/')
    else:
        form = BirthdayVoteForm()
    return render(request, 'name.html', {'form': form})


def get_something(request):
    if request.method == 'POST':
        form = BirthdayNoteForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thank_you/')
    else:
        form = BirthdayNoteForm()
    return render(request, 'notes.html', {'form': form})

