from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.urls import reverse
from django.contrib import messages
from .forms import NoteForm
from datetime import datetime
from .models import Note
from .forms import NoteForm
from .forms import SearchForm
from .forms import UserForm
from django.db.models import Q

def home(request):
    return render(request, 'home.html')

def imgpage(request):
    return render(request, "imagepage.html")

def num(request, number):
    return render(request, 'numgimmick.html',{"number" : number})

def signupView(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        try:
            if form.is_valid():
                user = form.save()
                login(request,user)
                messages.success(request, 'You have successfully signed in!')
                return redirect(reverse('home'))
            else:
                messages.error(request, 'Registration failed. Please correct the mistakes.')

        except Exception as e:
            messages.error(request,f'Failed to Sign up due unexpected error:{str(e)}')

    else: 
        form = UserForm()

    return render(request, 'signup.html',{'form':form})


def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm( request , data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request, 'You have successfully logged in!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Login failed. Please correct the errors.')

    else:
            form = AuthenticationForm()
    
    return render(request, 'login.html',{'form': form})

def logoutView(request):
    logout(request)
    return redirect('login')

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes')
    else:
        form = NoteForm()

    return render(request,'create_notes.html', {'form':form})

def notes_page(request):
    notes = Note.objects.all().order_by('-posted_time')
    return render(request, 'notes.html', {'notes':notes})
    

def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id) #defining the primary key as the note id to pass in the view
    if request.method == 'POST':
        note.delete()
    return redirect('notes')


def edit_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST,instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes')
        
    else:
        form = NoteForm(instance=note)
    return render(request, 'edit_note.html', {'form':form, 'note':note})



def search_bar(request):
    form = SearchForm(request.GET)
    results = []

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        notes = Note.objects.filter(Q(author__icontains=search_query) | Q(description__icontains=search_query))

        sorted_notes = sorted(
            notes,
            key=lambda note: note.author.startswith(search_query),
            reverse=True)

    results = [{'author':note.author,'description': note.description}for note in sorted_notes]
    return render(request,'notes.html',{'form':form,'results':results,'notes':notes})