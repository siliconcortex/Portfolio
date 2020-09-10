from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'podcast'

urlpatterns = [
    path('list/', views.PodcastListView.as_view(), name = 'list'),
    path('podcast/<pk>', views.EpisodeListView.as_view(), name='podcast'),
    path('episode/<pk>', views.EpisodeDetailView.as_view(), name = 'episode'),
]
