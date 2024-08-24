import requests, json, os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('APIKEY')
base_url = f'https://www.omdbapi.com/?apikey={API_KEY}&'

def get_movie_info(movie_name, year=None):
    url = base_url + f't={movie_name}' + (f'&y={year}' if year else '')
    response = requests.get(url).json()
    return response

def search_movies(query):
    url = base_url + f's={query}'
    response = requests.get(url).json()
    return response['Search'] if response['Response'] == 'True' else []