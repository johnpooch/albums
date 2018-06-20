from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Title(models.Model):

    owner = models.CharField(max_length=200, null=True)
    release_title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    genres = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    
    def __str__(self):
        return self.release_title