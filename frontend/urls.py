from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/', views.get_movie, name='movie_search'),
    path('search/<str:query>/', views.search_movies_view, name='search_movies')
]