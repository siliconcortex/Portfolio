from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    """Page Fields"""
    author = models.ForeignKey('auth.User', on_delete = models.PROTECT, blank = True)
    title = models.CharField(max_length = 200, blank = True)
    thumbnail = models.ImageField(upload_to = 'thumbnail/', blank = True)
    content_1 = models.TextField(blank = True)
    inline_1 = models.ImageField(upload_to='inlines/', blank = True)
    content_2 = models.TextField(blank = True)
    inline_2 = models.ImageField(upload_to='inlines/', blank = True)
    content_3 = models.TextField(blank = True)
    inline_3 = models.ImageField(upload_to='inlines/', blank = True)
    content_4 = models.TextField(blank = True)
    inline_4 = models.ImageField(upload_to='inlines/', blank = True)
    content_5 = models.TextField(blank = True)
    inline_5 = models.ImageField(upload_to='inlines/', blank = True)
    published_date = models.DateTimeField(default = timezone.now)


class Page(models.Model):
    """Page Fields"""
    author = models.ForeignKey('auth.User', on_delete = models.PROTECT, blank = True)
    title = models.CharField(max_length = 200, blank = True)
    thumbnail = models.ImageField(upload_to = 'thumbnail/', blank = True)
    content_1 = models.TextField(blank = True)
    inline_1 = models.ImageField(upload_to='inlines/', blank = True)
    content_2 = models.TextField(blank = True)
    inline_2 = models.ImageField(upload_to='inlines/', blank = True)
    content_3 = models.TextField(blank = True)
    inline_3 = models.ImageField(upload_to='inlines/', blank = True)
    content_4 = models.TextField(blank = True)
    inline_4 = models.ImageField(upload_to='inlines/', blank = True)
    content_5 = models.TextField(blank = True)
    inline_5 = models.ImageField(upload_to='inlines/', blank = True)
