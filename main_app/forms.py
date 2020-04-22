"""Importing the built in Django forms"""
from django import forms

"""Importing the models that we created"""
from main_app.models import (
    Post, Page
)


class PostForm(forms.ModelForm):
    #form fields go here
    class Meta:
        model = Post
        """"you can set the fields or you can set exclude"""
        fields = ['title', 'content', 'thumbnail']

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        exclude = ['author']
