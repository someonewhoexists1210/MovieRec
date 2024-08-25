from django.db import models
from django.core.validators import MaxValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField(null=True, validators=[MaxValueValidator(2100)])
    genre = models.CharField(max_length=50)
    plot = models.TextField(null=True)
    actors = models.TextField(null=True)
    language = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    rating = models.FloatField()
    image = models.URLField(null=True)
    
    def __str__(self):
        return self.title