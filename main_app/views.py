"""Importing models """
from main_app.models import Post

"""Import the forms"""
from main_app.forms import PostForm

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
    context_dict = {'posts_list': posts_list}
    return render(request, 'main_app/post_list.html', context_dict)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context_dict = {'post':post}
    return render(request, 'main_app/post_detail.html', context_dict)

@login_required
def post_create(request):
    if request.method == "POST":
    #request.POST =
    #<QueryDict: {'title': ['asdfasdf'], 'content': ['asdfasdf'],
    #'thumbnail': [''], 'csrfmiddlewaretoken': ['nZBRmCfNwQeV0eQEajwzEntxAJzio8jB0Iaf3mc6KLt5BkLgWTkywb4wHYA7Hoic']}>
        new_form = PostForm(request.POST)
        if new_form.is_valid():
            author = request.user
            title = new_form.cleaned_data['title']
            content = new_form.cleaned_data['content']
            thumbnail = new_form.cleaned_data['thumbnail']
            print(author, title, content)

            new_post = Post.objects.create(author=author, title = title, content = content, thumbnail = thumbnail)
            new_post.save()

    return render(request, 'main_app/post_create.html')
