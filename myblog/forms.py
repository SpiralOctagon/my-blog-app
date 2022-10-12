from django import forms
from django.forms import FileField, FileInput, ImageField, ModelForm, TextInput, Textarea
from .models import BlogPost, User

class NewBlog(ModelForm):
    class Meta:
        model = BlogPost
        fields = ('Title', 'Description')
        widgets = {
            'Title' : TextInput(attrs={'class': 'form-control'}),
            'Description' : Textarea(attrs={'cols': 55, 'rows': 10, 'class': 'form-control', 'style': 'resize: none'})
        }

class Login(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'Username' : TextInput(attrs={'class': 'form-control'}),
            'First Name' : TextInput(attrs={'class': 'form-control'}),
            'Last Name' : TextInput(attrs={'class': 'form-control'}),
            'Avatar': FileInput(attrs={'class': 'form-control'})
        }
        