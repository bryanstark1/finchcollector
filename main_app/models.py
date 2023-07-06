from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=60)
    breed = models.CharField(max_length=75)
    location = models.CharField(max_length=100)
    colors = models.CharField(max_length=100)