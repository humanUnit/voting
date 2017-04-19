from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import logout
from .forms import BirthdayVoteForm, BirthdayNoteForm


def get_voting(request):
    if request.method == 'POST':
        form = BirthdayVoteForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('polls:notes'))
    else:
        form = BirthdayVoteForm()
    return render(request, 'voting_form.html', {'form': form})


def get_notes(request):
    if request.method == 'POST':
        form = BirthdayNoteForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect(reverse('polls:thank_you'))

    else:
        form = BirthdayNoteForm()
    return render(request, 'notes_form.html', {'form': form})


def get_thank_you_page(request):
    return render(request, 'thank_you_page.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('polls:login'))



