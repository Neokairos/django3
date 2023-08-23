from django import forms 
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["author","description"]

class SearchForm(forms.Form):
    search_query = forms.CharField(label="Search", max_length=100)