from django.db import models
from django.utils import timezone
from django.urls import reverse
from uuid import uuid4



# Create your models here.
class Post(models.Model):
    """post fields"""
    uuid = uuid4().int
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnail/')
    published_date = models.DateTimeField(default = timezone.now)

    def get_absolute_url(self):
        """this code is telling django what to do after
        creating this model"""
        return reverse('post_detail', kwargs={'pk':self.pk})

    def __str__(self):
        """this function tells python what to do if we print this
        Post model"""
        return self.title
