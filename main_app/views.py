from django.shortcuts import render

""""These imports are used to import the Built-in Views django
has """
from django.views.generic import (
    TemplateView, ListView, DetailView,
    CreateView, UpdateView, DeleteView,
    )

"""Importing models """
from main_app.models import Post

"""Import the forms"""
from main_app.forms import PostForm

"""Import the class-based-view login required
Import the function-based-view login required"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

"""Import the reverse and reverse_lazy functions"""
from django.urls import reverse, reverse_lazy

"""Importi the render, get_object_or_404, and redirect"""
from django.shortcuts import render, get_object_or_404, redirect

"""Import timezone function"""
from django.utils import timezone

class PostListView(ListView):
    """View that will display the posts as a list and will serve as a main blog page"""
    model = Post

    def get_queryset(self):
        """This function runs when the list is generated,
        and is sorting by published date, descending"""
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    """View that will display the posts content in detail"""
    model = Post
