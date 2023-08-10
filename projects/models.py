from django.db import models
from django.utils import timezone



class Note(models.Model):
    author = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    posted_time = models.DateTimeField(default=timezone.now)


