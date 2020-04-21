"""Importing the built in Django forms"""
from django import forms

"""Importing the models that we created"""
from main_app.models import (
    Post,
)


class PostForm(forms.ModelForm):
    #form fields go here
    class Meta:
        model = Post
        """OPTIONS: ___all___ , ['include', ...], ('exclude', ...)"""
        fields = ['title', 'content', 'thumbnail']
