from django.db import models
from django.utils import timezone

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length= 255)
    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length= 255)
    release_year = models.IntegerField()
    number_in_stuck = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre , on_delete= models.CASCADE)
    Date_created = models.DateField(default= timezone.now)
    
    def __str__(self):
        return self.title