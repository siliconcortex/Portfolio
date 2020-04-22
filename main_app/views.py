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
    context_dict = {'post':post, 'pages_list':pages_list}
    return render(request, 'main_app/post_detail.html', context_dict)

def page_detail(request, pk):
    pages_list = Page.objects.order_by('title')
    page = Page.objects.get(pk=pk)
    context_dict = {'page':page, 'pages_list':pages_list}
    return render(request, 'main_app/page_detail.html', context_dict)

@login_required
def post_create(request):
    pages_list = Page.objects.order_by('title')
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

    return render(request, 'main_app/post_create.html', {'pages_list':pages_list})

@login_required
def page_create(request):
    pages_list = Page.objects.order_by('title')
    if request.method == "POST":
        new_form = PageForm(request.POST)
        if new_form.is_valid():
            author = request.user
            title = new_form.cleaned_data['title']
            thumbnail = new_form.cleaned_data['thumbnail']
            content_1 = new_form.cleaned_data['content_1']
            inline_1 = new_form.cleaned_data['inline_1']
            content_2 = new_form.cleaned_data['content_2']
            inline_2 = new_form.cleaned_data['inline_2']
            content_3 = new_form.cleaned_data['content_3']
            inline_3 = new_form.cleaned_data['inline_3']
            content_4 = new_form.cleaned_data['content_4']
            inline_4 = new_form.cleaned_data['inline_4']
            content_5 = new_form.cleaned_data['content_5']
            inline_5 = new_form.cleaned_data['inline_5']

            new_page = Page.objects.create(
                author = author,
                title = title,
                thumbnail = thumbnail,
                content_1 = content_1,
                inline_1 = inline_1,
                content_2 = content_2,
                inline_2 = inline_2,
                content_3 = content_3,
                inline_3 = inline_3,
                content_4 = content_4,
                inline_4 = inline_4,
                content_5 = content_5,
                inline_5 = inline_5,
            )

            new_page.save()

    return render(request, 'main_app/page_create.html', {'page_list':pages_list})
