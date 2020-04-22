"""Importing the built in Django forms"""
from django import forms

"""Importing the models that we created"""
from main_app.models import (
    Post, Page
)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = '__all__'
