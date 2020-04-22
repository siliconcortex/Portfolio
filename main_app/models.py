from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    """post fields"""
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnail/%Y%m%d/', blank = True)
    published_date = models.DateTimeField(default = timezone.now)

    def get_absolute_url(self):
        """this code is telling django what to do after
        creating this model"""
        return reverse('post_detail', kwargs={'pk':self.pk})

    def __str__(self):
        """this function tells python what to do if we print this
        Post model"""
        return self.title

class Page(models.Model):
    """Page Fields"""
    author = models.ForeignKey('auth.User', on_delete = models.PROTECT)
    title = models.CharField(max_length = 200)
    thumbnail = models.ImageField('inlines/%Y%m%d/', blank = True)
    content_1 = models.TextField(blank = True)
    inline_1 = models.ImageField(upload_to='inlines/%Y%m%d/', blank = True)
    content_2 = models.TextField(blank = True)
    inline_2 = models.ImageField(upload_to='inlines/%Y%m%d/', blank = True)
    content_3 = models.TextField(blank = True)
    inline_3 = models.ImageField(upload_to='inlines/%Y%m%d/', blank = True)
    content_4 = models.TextField(blank = True)
    inline_4 = models.ImageField(upload_to='inlines/%Y%m%d/', blank = True)
    content_5 = models.TextField(blank = True)
    inline_5 = models.ImageField(upload_to='inlines/%Y%m%d/', blank = True)
