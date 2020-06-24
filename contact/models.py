from django.db import models

# Create your models here.
class Email(models.Model):
    sender_email = models.EmailField()
    message = models.TextField(max_length = 2000)
