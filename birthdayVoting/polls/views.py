# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.core.checks import messages
from django.core.mail import EmailMessage
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse
from django.contrib.auth import authenticate, login, update_session_auth_hash

from .models import Choices, Notes
from .forms import BirthdayVoteForm, BirthdayNoteForm, UserRegistrationForm, UserForm, ProfileForm


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
        if not Notes.objects.filter(user=request.user).exists():
            return HttpResponseRedirect(reverse('polls:notes'))
        if Notes.objects.filter(user=request.user).exists():
            return HttpResponseRedirect(reverse('polls:thank_you'))
    else:
        return render(request, 'choice_made.html')


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
                    to=['yuriy.ovcharenko@castingnetworks.com', 'aleksander.sukharev@castingnetworks.com',
                        'ruslan.nescheret@castingnetworks.com', 'ekaterina.kelembet@castingnetworks.com',
                        'ihor.maslov@castingnetworks.com', 'oleksandr.yemets@castingnetworks.com',
                        'sergii.kalinichenko@castingnetworks.com', 'vlad.tertyshnyi@castingnetworks.com',
                        'andrey.makhonin@castingnetworks.com', 'maxim.tsapenko@castingnetworks.com'],
                    headers={'Reply-To': 'votingappteam@gmail.com'}
                )
                email.send()
                return HttpResponseRedirect(reverse('polls:thank_you'))
    else:
        form = BirthdayNoteForm()
    return render(request, 'notes_form.html', {'form': form})


@login_required
def get_note(request):
    if request.method == 'POST':
        if not Choices.objects.filter(user=request.user).exists():
            return HttpResponseRedirect(reverse('polls:voting'))
        if Choices.objects.filter(user=request.user).exists():
            return HttpResponseRedirect(reverse('polls:thank_you'))
    else:
        return render(request, 'notes_made.html')


@login_required
def get_thank_you_page(request, ):
    return render(request, 'thank_you_page.html')


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.Info(request, 'Your profile was successfully updated!')
            return redirect('polls:profile')
        else:
            messages.Error(request, 'Error')
    else:
        if Choices.objects.filter(user=request.user).exists() and Notes.objects.filter(user=request.user).exists():
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
            user = request.user
            choice = Choices.objects.get(user=user)
            notes = Notes.objects.get(user=user)
            return render(request, 'profile.html', {
                'choice': choice,
                'notes': notes,
                'user_form': user_form,
                'profile_form': profile_form,
            })

        if Notes.objects.filter(user=request.user).exists():
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
            user = request.user
            notes = Notes.objects.get(user=user).notes_field
            return render(request, 'profile.html', {
                'user_form': user_form,
                'profile_form': profile_form,
                'notes': notes
            })
        if Choices.objects.filter(user=request.user).exists():
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
            user = request.user
            choice = Choices.objects.get(user=user)
            return render(request, 'profile.html', {
                'choice': choice,
                'user_form': user_form,
                'profile_form': profile_form,
            })

        if not Choices.objects.filter(user=request.user).exists() and not Notes.objects.filter(
                user=request.user).exists():
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
            return render(request, 'profile.html', {
                'user_form': user_form,
                'profile_form': profile_form,
            })


@login_required
def get_admin(request):
    users = User.objects.order_by('username')
    user = request.user
    last_seen = user.last_login.date()
    return render(request, 'admin.html', {
        'users': users,
        'last_seen': last_seen,
    })


@login_required
def delete_user(request, user_id):
    if request.user.id == int(user_id):
        User.objects.get(id=user_id).delete()
        return HttpResponseRedirect(reverse('polls:admin'))
    if request.user.id != int(user_id):
        message = request.user.id
        return render(request, 'admin.html', {
            'mm': message,
        })
    return render(request, 'admin.html')


@login_required
def delete_choice(request):
    try:
        Choices.objects.get(user=request.user).delete()
    except:
        pass
    return HttpResponseRedirect(reverse('polls:profile'))


@login_required
def delete_notes(request):
    try:
        Notes.objects.get(user=request.user).delete()
    except:
        pass
    return HttpResponseRedirect(reverse('polls:profile'))


@login_required
def get_settings(request):
    return render(request, 'settings.html', {
        'notes': Notes.objects.all(),
    })


@login_required
def create_notes_field(request):
    Notes.objects.create()
    if request.POST:
        Notes.objects.create(notes_field=request.POST.get('notes'), user=request.user)
    return render(request, 'notes_form.html', {
        'notes': Notes.objects.all(),
    })


@login_required
def delete_notes_field(request):
    Notes.objects.all().delete()
    return render(request, 'settings.html', {
        'notes': Notes.objects.all(),
    })


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.Info(request, 'Your password was successfully updated!')
            return redirect('polls:change_password')
        else:
            messages.Error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })
