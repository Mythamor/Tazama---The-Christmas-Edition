from django.urls import path
from .views import home, MovieSearch, recommend

urlpatterns = [
    path("", home, name="movies-home"),
    path('search/', MovieSearch.as_view(), name='movie_search'),
    path('recommend/', recommend, name='movie_recommend'),
]
