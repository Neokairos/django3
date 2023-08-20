from django.db import models
from django.utils import timezone



class Note(models.Model):
    author = models.CharField(max_length=20, blank=True)
    description = models.TextField()
    posted_time = models.DateTimeField(default=timezone.now)


