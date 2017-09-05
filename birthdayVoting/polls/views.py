# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.core.checks import messages
from django.core.mail import EmailMessage
from django.db import transaction
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Choices, Notes, ChoicesCreate
from .forms import BirthdayVoteForm, BirthdayNoteForm, UserRegistrationForm, UserForm, ProfileForm, CreateChoiceForm


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
                notes = Notes.objects.filter(user=user)
                for note in notes:
                    print note.notes_field
                context = {
                    'contact_name': user.username,
                    'contact_email': user.email,
                    'choice': Choices.objects.get(user=user).get_choice_fields_display(),
                    'notes': notes if Notes.objects.filter(
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
    BirthdayNoteFormSet = modelformset_factory(Notes, BirthdayNoteForm, extra=1)
    if request.method == 'POST':
        formset = BirthdayNoteFormSet(request.POST)
        if formset.is_valid():
            if not Choices.objects.filter(user=request.user).exists():
                notes = formset.save(commit=False)
                for note in notes:
                    user = request.user
                    note.user = user
                    note.save()
                    print note.save()
                return HttpResponseRedirect(reverse('polls:voting'))
            if Choices.objects.filter(user=request.user).exists():
                notes = formset.save(commit=False)
                for note in notes:
                    user = request.user
                    note.user = user
                    note.save()
                    print note.save()
                template = get_template('contact_template')
                user = request.user
                notes = Notes.objects.filter(user=user)
                for note in notes:
                    print note.notes_field
                context = {
                    'contact_name': user.username,
                    'contact_email': user.email,
                    'choice': Choices.objects.get(user=user).get_choice_fields_display(),
                    'notes': notes if Notes.objects.filter(
                        user=user).exists() else 'User left field empty',
                }
                content = template.render(context, request)
                email = EmailMessage(
                    "Someone's birthday soon",
                    content,
                    "Birthday voting" + '',
                    to=['ekaterina.kelembet@castingnetworks.com', ],
                    headers={'Reply-To': 'votingappteam@gmail.com'}
                )
                email.send()
                return HttpResponseRedirect(reverse('polls:thank_you'))
    else:
        formset = BirthdayNoteFormSet()
    return render(request, 'notes_form.html', {'formset': formset})


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
    user = request.user
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.Info(request, 'Your profile was successfully updated!')
            return redirect('polls:profile')
        else:
            messages.Error(request, 'Error')
    else:
        if Choices.objects.filter(user=user).exists() and Notes.objects.filter(user=user).exists():
            user_form = UserForm(instance=user)
            profile_form = ProfileForm(instance=user.profile)
            choice = Choices.objects.get(user=user)
            notes = Notes.objects.filter(user=user)
            for note in notes:
                print note.notes_field
            return render(request, 'profile.html', {
                'choice': choice,
                'notes': notes,
                'user_form': user_form,
                'profile_form': profile_form,
            })

        if Notes.objects.filter(user=user).exists():
            user_form = UserForm(instance=user)
            profile_form = ProfileForm(instance=user.profile)
            notes = Notes.objects.filter(user=user)
            for note in notes:
                print note.notes_field
            return render(request, 'profile.html', {
                'user_form': user_form,
                'profile_form': profile_form,
                'notes': notes
            })
        if Choices.objects.filter(user=user).exists():
            user_form = UserForm(instance=user)
            profile_form = ProfileForm(instance=user.profile)
            choice = Choices.objects.get(user=user)
            return render(request, 'profile.html', {
                'choice': choice,
                'user_form': user_form,
                'profile_form': profile_form,
            })

        if not Choices.objects.filter(user=request.user).exists() and not Notes.objects.filter(
                user=user).exists():
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
    user = request.user
    if user.is_superuser:
        User.objects.get(id=user_id).delete()
        return HttpResponseRedirect(reverse('polls:admin'))
    if request.user.id == int(user_id):
        User.objects.get(id=user_id).delete()
        return HttpResponseRedirect(reverse('polls:admin'))
    if request.user.id != int(user_id) and not user.is_superuser:
        message = request.user.id
        users = User.objects.order_by('username')
        last_seen = user.last_login.date()
        return render(request, 'admin.html', {
            'mm': message,
            'users': users,
            'last_seen': last_seen,
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
def delete_notes(request, notes_id):
    Notes.objects.get(id=notes_id).delete()
    return HttpResponseRedirect(reverse('polls:profile'))


@login_required
def get_settings(request):
    CreateChoiceFormSet = modelformset_factory(ChoicesCreate, CreateChoiceForm, extra=1)
    if request.method == 'POST':
        formset = CreateChoiceFormSet(request.POST)
        if formset.is_valid():
            choices = formset.save(commit=False)
            for choice in choices:
                user = request.user
                choice.user = user
                choice.save()
                print choice.save()
                print ChoicesCreate.objects.all()
    else:
        formset = CreateChoiceFormSet()
    return render(request, 'settings.html', {
        'choice_form': CreateChoiceForm(request.POST, request.user),
        'notes': Notes.objects.all(),
        'choice_field': ChoicesCreate.objects.all(),
        'formset': formset
    })


@login_required
def create_notes_field(request):
    Notes.objects.create()
    return HttpResponseRedirect(reverse('polls:settings'))


@login_required
def delete_notes_field(request, notes_id):
    Notes.objects.get(id=notes_id).delete()
    return HttpResponseRedirect(reverse('polls:settings'))


@login_required
@csrf_exempt
def change_password(request):
    if request.is_ajax() and request.method == 'POST':
        print request.user, request.POST
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            # messages.Info(request, 'Your password was successfully updated!')
            message = 'Your password was successfully updated!'
        else:
            message = 'Form is invalid %s!' % form.errors

    else:
        message = 'Please correct the error below.'
        # messages.Error(request, 'Please correct the error below.')
    return HttpResponse(json.dumps({'data': message}), 'application/json')


@login_required
def create_choice_field(request):
    ChoicesCreate.objects.create()
    print ChoicesCreate.objects.all()
    return HttpResponseRedirect(reverse('polls:settings'))


@login_required
def delete_choice_field(request, choice_id):
    ChoicesCreate.objects.get(id=choice_id).delete()
    return HttpResponseRedirect(reverse('polls:settings'))








