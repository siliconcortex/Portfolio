"""Importing models """
from main_app.models import Post, Page

"""Import the forms"""
from main_app.forms import PostForm, PageForm

"""Import the class-based-view login required
Import the function-based-view login required"""
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

"""Import the reverse and reverse_lazy functions"""
from django.urls import reverse, reverse_lazy

"""Importi the render, get_object_or_404, and redirect"""
from django.shortcuts import render, get_object_or_404, redirect

"""Import timezone function"""
from django.utils import timezone

def post_list(request):
    posts_list = Post.objects.order_by('-published_date')
    pages_list = Page.objects.order_by('title')
    context_dict = {
        'posts_list': posts_list,
        'pages_list':pages_list,
    }
    return render(request, 'main_app/post_list.html', context_dict)

def post_detail(request, pk):
    pages_list = Page.objects.order_by('title')

    post = Post.objects.get(pk=pk)
    context_dict = {
        'post':post,
        'pages_list':pages_list,
        }
        
    return render(request, 'main_app/post_detail.html', context_dict)

def page_detail(request, pk):
    pages_list = Page.objects.order_by('title')

    page = Page.objects.get(pk=pk)
    context_dict = {
        'page':page,
        'pages_list':pages_list,
        }
    return render(request, 'main_app/page_detail.html', context_dict)
