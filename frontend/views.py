import json
from .models import Movie
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .request_send import get_movie_info

# Create your views here.
def index(request):
    return render(request, 'index.html')

def get_movie(request):
    name = request.POST["movie_title"]
    year = request.POST["movie_year"]
    if Movie.objects.filter(title=name).exists():
        movie = Movie.objects.get(title=name)
        return render(request, 'movie.html', {'movie': movie})
    data = get_movie_info(name, year)
    if data['Response'] == 'False':
        return HttpResponse(data['Error'])
    if data['imdbRating'] == 'N/A':
        data['imdbRating'] = 0
    movie = Movie(
        title=data['Title'], 
        year=data['Year'],
        genre=data['Genre'], 
        language=data['Language'], 
        country=data['Country'], 
        rating=data['imdbRating'],
        image=data['Poster']
    )
    movie.save()
    return render(request, 'movie.html', {'movie': movie})
