from django.shortcuts import render

# Create your views here.

from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Episode, Podcast
from main_app.models import Post, Page

class PodcastListView(ListView):
    model = Podcast
    paginate_by = 10

    posts_list = Post.objects.order_by('-published_date')
    pages_list = Page.objects.order_by('title')
    extra_context = {
        'posts_list': posts_list,
        'pages_list':pages_list,
    }

class EpisodeListView(ListView):
    #model = Episode
    paginate_by = 10  # if pagination is desired

    posts_list = Post.objects.order_by('-published_date')
    pages_list = Page.objects.order_by('title')
    extra_context = {
        'posts_list': posts_list,
        'pages_list':pages_list,
    }

    def get_queryset(self, **kwargs):
        podcast = Podcast.objects.get(pk = self.kwargs.get('pk'))
        return Episode.objects.filter(podcast = podcast)


class EpisodeDetailView(DetailView):
    model = Episode
    posts_list = Post.objects.order_by('-published_date')
    pages_list = Page.objects.order_by('title')
    extra_context = {
        'posts_list': posts_list,
        'pages_list':pages_list,
    }
