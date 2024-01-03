from django.db import models

# Create your models here.

class Link(models.Model):
    url = models.URLField(max_length=5000)
    identifier = models.CharField(max_length=15)