from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username

class UserPreferences(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    rating = models.FloatField()
    
    def __str__(self):
        return self.user.username
    
class Movie(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    rating = models.FloatField()
    
    def __str__(self):
        return self.title