# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import get_template
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .models import Choices, Notes
from .forms import BirthdayVoteForm, BirthdayNoteForm, UserRegistrationForm


def get_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.user = authenticate(username=form.cleaned_data['username'],
                                         password=form.cleaned_data['password1'], )
            login(request, new_user)
            return HttpResponseRedirect(reverse('polls:voting'))
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def get_voting(request):
    if Choices.objects.filter(user=request.user).exists():
        return HttpResponseRedirect(reverse('polls:choice_made'))
    if request.method == 'POST':
        form = BirthdayVoteForm(request.POST)
        if form.is_valid():
            if Notes.objects.filter(user=request.user).exists():
                vote = form.save(commit=False)
                user = request.user
                vote.user = user
                vote.save()
                context = {
                    'contact_name': user.username,
                    'contact_email': user.email,
                    'choice': Choices.objects.get(user=user).get_choice_fields_display(),
                    'notes': Notes.objects.get(user=user).notes_field if Notes.objects.filter(
                        user=user).exists() else 'User left field empty',
                }
                template = get_template('contact_template')
                content = template.render(context, request)
                email = EmailMessage(
                    "Someone's birthday soon",
                    content,
                    "Birthday voting" + '',
                    to=['katyakelembet@gmail.com'],
                    headers={'Reply-To': 'katyakelembet@gmail.com'}
                )
                email.send()
                return HttpResponseRedirect(reverse('polls:thank_you'))
            if not Notes.objects.filter(user=request.user).exists():
                vote = form.save(commit=False)
                user = request.user
                vote.user = user
                vote.save()
                return HttpResponseRedirect(reverse('polls:notes'))
    else:
        form = BirthdayVoteForm()
    return render(request, 'voting_form.html', {'form': form})


@login_required
def get_choices(request):
    if request.method == 'POST':
        form = BirthdayVoteForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('polls:notes'))
    else:
        form = BirthdayVoteForm()
        return render(request, 'choice_made.html', {'form': form})


@login_required
def get_notes(request):
    if Notes.objects.filter(user=request.user).exists():
        return HttpResponseRedirect(reverse('polls:notes_made'))
    if request.method == 'POST':
        form = BirthdayNoteForm(request.POST)
        if form.is_valid():
            if not Choices.objects.filter(user=request.user).exists():
                notes = form.save(commit=False)
                user = request.user
                notes.user = user
                notes.save()
                return HttpResponseRedirect(reverse('polls:voting'))
            if Choices.objects.filter(user=request.user).exists():
                notes = form.save(commit=False)
                user = request.user
                notes.user = user
                notes.save()
                template = get_template('contact_template')
                user = request.user
                context = {
                    'contact_name': user.username,
                    'contact_email': user.email,
                    'choice': Choices.objects.get(user=user).get_choice_fields_display(),
                    'notes': Notes.objects.get(user=user).notes_field if Notes.objects.filter(
                        user=user).exists() else 'User left field empty',
                }
                content = template.render(context, request)
                email = EmailMessage(
                    "Someone's birthday soon",
                    content,
                    "Birthday voting" + '',
                    to=['katyakelembet@gmail.com'],
                    headers={'Reply-To': 'katyakelembet@gmail.com'}
                )
                email.send()
                return HttpResponseRedirect(reverse('polls:thank_you'))
    else:
        form = BirthdayNoteForm()
    return render(request, 'notes_form.html', {'form': form})


@login_required
def get_note(request):
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('polls:thank_you'))
    else:
        return render(request, 'notes_made.html')


@login_required
def get_thank_you_page(request, ):
    return render(request, 'thank_you_page.html')
