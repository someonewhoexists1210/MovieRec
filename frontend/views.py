from django.http import HttpResponse
from django.shortcuts import render
from request_send import get_movie_info

# Create your views here.
def index(request):
    return get_movie_info('The Dark Knight')
    return HttpResponse("Hello, world. You're at the frontend index.")