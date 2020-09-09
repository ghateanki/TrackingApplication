from django import forms
from . models import Task

class PostForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title' , 'task' , 'author' , 'description', 'start', 'end')


class EditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title' , 'task' , 'description')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'This is title Placeholder Project'}),
            'task': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),

        }

