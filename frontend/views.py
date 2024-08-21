import json
from .models import Movie
from django.http import HttpResponse
from django.shortcuts import render
from .request_send import get_movie_info

# Create your views here.
def index(request, name):
    if Movie.objects.filter(title=name).exists():
        movie = Movie.objects.get(title=name)
        return render(request, 'index.html', {'movie': movie})
    data = get_movie_info(name)
    movie = Movie(
        title=data['Title'], 
        genre=data['Genre'], 
        language=data['Language'], 
        country=data['Country'], 
        rating=data['imdbRating']
    )
    movie.save()
    return render(request, 'index.html', {'movie': movie})
