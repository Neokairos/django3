from django import forms 
from .models import Note, CustomUserModel


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["author","description"]

class SearchForm(forms.Form):
    search_query = forms.CharField(label="Search", max_length=100)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUserModel
        fields = ('username','password')