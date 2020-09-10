from django.db import models
from django.utils import timezone

# Create your models here.
class Podcast(models.Model):
    title = models.CharField(max_length = 100)
    url = models.CharField(max_length = 1000)
    language = models.CharField(max_length = 50, default = 'English')
    subtitle = models.CharField(max_length = 100)
    creator = models.CharField(max_length = 100, default = 'Leslie Caminade')
    description = models.CharField(max_length = 200)

    keyword1 = models.CharField(max_length = 50, blank = True)
    keyword2 = models.CharField(max_length = 50, blank = True)
    keyword3 = models.CharField(max_length = 50, blank = True)
    keyword4 = models.CharField(max_length = 50, blank = True)
    keyword5 = models.CharField(max_length = 50, blank = True)
    keyword6 = models.CharField(max_length = 50, blank = True)
    keyword7 = models.CharField(max_length = 50, blank = True)
    keyword8 = models.CharField(max_length = 50, blank = True)
    keyword9 = models.CharField(max_length = 50, blank = True)
    keyword10 = models.CharField(max_length = 50, blank = True)

    email = models.EmailField()
    image = models.ImageField(upload_to = 'podcast/thumbnails')

    category1 = models.CharField(max_length = 50, blank = True)
    category2 = models.CharField(max_length = 50, blank = True)
    category3 = models.CharField(max_length = 50, blank = True)

class Episode(models.Model):
    podcast = models.ForeignKey(Podcast,on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)
    subtitle = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'podcast/thumbnails')
    length = models.CharField(max_length = 50)
    duration = models.CharField(max_length = 50)
    season = models.CharField(max_length = 10)
    episode = models.CharField(max_length = 10)

    file = models.FileField(upload_to = 'podcast/files')
    published_date = models.DateField(default = timezone.now)
    explicit = models.CharField(max_length = 10 ,default = 'NO')

    def generate_feed(self):
        fg = FeedGenerator()
        fg.id('http://lernfunk.de/media/654321')
        fg.title('Some Testfeed')
        fg.author( {'name':'John Doe','email':'john@example.de'} )
        fg.link( href='http://example.com', rel='alternate' )
        fg.logo('http://ex.com/logo.jpg')
        fg.subtitle('This is a cool feed!')
        fg.link( href='http://larskiesow.de/test.atom', rel='self' )
        fg.language('en')
