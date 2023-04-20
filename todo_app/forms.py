from django import forms
from .models import Todo

#dans le dossier todo_app/forms.py
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
