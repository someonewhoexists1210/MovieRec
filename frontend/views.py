import json
from .models import Movie
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .request_send import get_movie_info, search_movies

# Create your views here.
def index(request):
    return render(request, 'index.html')

def search_movies_view(request, query):
    movies = search_movies(query)

    for i in range(len(movies)):
        if Movie.objects.filter(title=movies[i]['Title']).exists():
            movies[i] = Movie.objects.get(title=movies[i]['Title'])
        else:
            mov = get_movie_info(movies[i]['Title'], movies[i]['Year'])
            if '–' in mov['Year']:
                mov['Year'] = mov['Year'].split('–')[0]
            movie = Movie(
                title=mov['Title'],
                year=mov['Year'],
                genre=mov['Genre'],
                language=mov['Language'],
                country=mov['Country'],
                rating=mov['imdbRating'],
                image=mov['Poster']
            )
            movie.save()
            movies[i] = movie
        

    return render(request, 'search.html', {'movies': movies})

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
        plot=data['Plot'],
        actors=data['Actors'],
        language=data['Language'], 
        country=data['Country'], 
        rating=data['imdbRating'],
        image=data['Poster']
    )
    movie.save()
    return render(request, 'movie.html', {'movie': movie})

def filter_movies(request):
    if request.method == 'POST':
        genre = request.POST["genre"]
        year = request.POST["year"]
        rating = request.POST["rating"]
        movies = Movie.objects.all()
        language = request.POST["language"]
        if genre != 'all':
            movies = movies.filter(genre__contains=genre)
        if year != 'all':
            if year == 'older':
                movies = movies.filter(year__lt=2019)
            movies = movies.filter(year=year)
        if rating != 'all':
            movies = movies.filter(rating__gte=float(rating))
        if language != 'all':
            movies = movies.filter(language__contains=language)

        movies = movies.order_by('-rating')
        return render(request, 'search.html', {'movies': movies})
    
    return render(request, 'filter.html')