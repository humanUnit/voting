from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Choices, Notes
from .forms import BirthdayVoteForm, BirthdayNoteForm


@login_required
def get_voting(request):
    if Choices.objects.filter(user=request.user).exists():
        return HttpResponseRedirect(reverse('polls:notes'))
    if request.method == 'POST':
        form = BirthdayVoteForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            user = request.user
            vote.user = user
            vote.save()
            return HttpResponseRedirect(reverse('polls:notes'))
    else:
        form = BirthdayVoteForm()
    return render(request, 'voting_form.html', {'form': form})


@login_required
def get_notes(request):
    if Notes.objects.filter(user=request.user).exists():
        return HttpResponseRedirect(reverse('polls:thank_you'))
    if request.method == 'POST':
        form = BirthdayNoteForm(request.POST)
        if form.is_valid():
            notes = form.save(commit=False)
            user = request.user
            notes.user = user
            notes.save()
            return HttpResponseRedirect(reverse('polls:thank_you'))
    else:
        form = BirthdayNoteForm()
    return render(request, 'notes_form.html', {'form': form})


@login_required
def get_thank_you_page(request):
    return render(request, 'thank_you_page.html')






