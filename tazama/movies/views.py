import os
import requests
import random
from functools import reduce
from operator import or_
from django.shortcuts import render
from django.http import HttpResponse
from typing import Any
from django.db import models
from django.core.cache import cache
from django.db.models.query import QuerySet, Q
from django.http import JsonResponse
from django.template.loader import render_to_string


# Create your views here.
from django.views.generic import View
from .models import Movie, Genre


# Import recommendation engine libraries
import pandas as pd
import pickle
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


API_KEY = ""


def home(request):
    return render(request, 'movies/home.html')


def get_movie_details(movie):
    cache_key = f"movie_details_{movie.tmdb_id}"
    cached_details = cache.get(cache_key)

    if cached_details:
        return cached_details
    

    url = f'https://api.themoviedb.org/3/movie/{movie.tmdb_id}?api_key={API_KEY}&language=en-US'
    response = requests.get(url)
    movie_detail = response.json()
    
    # Add details to the list
    details_list = {
        'title': movie.title,
        'poster_url': f"https://image.tmdb.org/t/p/w500/{movie_detail.get('poster_path','')}",
        'genre_names': ', '.join(genre.name for genre in movie.genres.all()),
        'tagline': movie_detail.get('tagline', ''),  # Get the tagline or an empty string if empty
    }

# Cache the details for future use
    cache.set(cache_key, details_list)

    return details_list


class MovieSearch(View):
    max_suggestions = 20

    def get_dataframe(self):
        # Load your DataFrame (replace 'your_dataframe.csv' with the actual file path)
        df = pd.read_csv('recommendation_engine/movie_data.csv')
        return df

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            # Filter movies based on the DataFrame column 'genres'
            df = self.get_dataframe()

            # Drop rows with missing values in the 'genres' column
            df = df.dropna(subset=['genres'])

            # Filter movies based on the cleaned 'genres' column
            genres_matching_query = df[df['genres'].str.contains(query, case=False)]

            # Create a list of genres
            suggestions = genres_matching_query['genres'].tolist()
        else:
            suggestions = []

        return JsonResponse({'data': suggestions}, safe=False)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return queryset


    

def recommend(request):
     # Load movies from the dataframe
    movie_list = pd.read_pickle('recommendation_engine/movie_list.pkl')

    # Fetch the genre from the request parameters
    genre = request.GET.get('query', '')

    # Filter movies based on the specified genre
    matching_movies = movie_list[movie_list["genres"].str.contains(genre, case=False)]

    recommend_list = []

    if not matching_movies.empty:
        # Shuffle the DataFrame to get a random order
        shuffled_movies = matching_movies.sample(frac=1)

        # Select a random sample of 5 movies
        for tmdb_id in shuffled_movies['tmdb_id'].tolist()[:5]:
            # Fetch data via API
            url = f'https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={API_KEY}&language=en-US'
            response = requests.get(url)
            movie_detail = response.json()

            # Add details to the list
            recommend_list.append({
                'title': movie_detail.get('title', ''),
                'poster_url': f"https://image.tmdb.org/t/p/w500/{movie_detail.get('poster_path', '')}",
            })

    # Return the details list to be displayed in the template
    return render(request, 'movies/movie_reco.html', {'details_list': recommend_list})
    

