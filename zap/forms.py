from dataclasses import fields
from pyexpat import model
from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta():

        model = Post
        fields = '__all__'