from django import forms
from . import models

class EmailForm(forms.ModelForm):
    class Meta:
        model = models.Email
        fields = '__all__'
