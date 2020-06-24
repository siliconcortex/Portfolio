from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                DeleteView, CreateView,
                                UpdateView)
from . import models
from . import forms

from datetime import datetime
from .standard_email import send_email

import requests

# Create your views here.
class EmailView(View):
    def get(self, *args, **kwargs):
        template_name = 'contact/contact.html'

        context = {
            'form': forms.EmailForm,
        }
        return render(self.request, template_name, context)

    def post(self, *args, **kwargs):
        SECRET_KEY = '6LfOxagZAAAAABjpaUt18E-hmlOtUFD4pyL-nj25'
        recaptcha_response = self.request.POST.get('g-recaptcha-response') #get ggoogle recapthcha response from form
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data = {
            'secret': SECRET_KEY,
            'response': recaptcha_response,
        })

        r = r.json()
        if r['success'] == 'false':
            return render(self.request, 'contact/failed.html')
            pass
        else:
            sender = self.request.POST.get('sender_email')
            message = self.request.POST.get('message')
            send_email(sender, message)
            return render(self.request, 'contact/success.html')
