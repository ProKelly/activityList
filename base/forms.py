
from django import forms
from base.models import ToDo

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        exclude = ('created', 'updated',)
        widgets = {
            'name':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'enter todo',
            }),
            'image':forms.FileInput(attrs={
                'class' : 'form-control',
            }),
        }
