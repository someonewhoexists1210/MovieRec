import requests, json, os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('APIKEY')
base_url = f'https://www.omdbapi.com/?apikey={API_KEY}&'

def get_movie_info(movie_name):
    url = base_url + f't={movie_name}'
    response = requests.get(url).json()
    return response