from contextlib import nullcontext
from django.db import models


# Create your models here.

class User(models.Model):

    Username = models.CharField(max_length=32)
    firstName = models.CharField(max_length=32, name="First Name")
    lastName = models.CharField(max_length=32, name="Last Name")
    PFP = models.ImageField(upload_to='pfp/', blank=True, name="Avatar")

    def __str__(self):
        return str(self.Username)

class BlogPost(models.Model):

    Title = models.CharField(max_length=48, name='Title')
    Description = models.CharField(max_length=2048, name='Description')

    def __str__(self):
        return str(self.date)
