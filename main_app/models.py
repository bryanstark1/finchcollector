from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=60)
    breed = models.CharField(max_length=75)
    location = models.CharField(max_length=100)
    colors = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})