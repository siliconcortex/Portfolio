"""Importing the built in Django forms"""
from django import forms

"""Importing the models that we created"""
from main_app.models import (
    Post,
)

"""creating PostForm - the form equivalent of the Post model"""
class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('title', 'content', 'thumbnail')

        """This widgets attribute allows us to specify the fields
        declared above and append HTML attributes to them such as
        in the case here, classes(we can also apply bootstrap
        classes here but we will add that later)"""
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinput'}),
            'content':forms.Textarea(attrs={'class':'textarea'}),
            'thumbnail':forms.FileInput(attrs={'class':'imageinput', 'accept':'image/*'})
        }
