from django.urls import path
from rest_api.views import peliculas,movie
from .viewsLogin import login

urlpatterns = [
    path('pelicula/', peliculas, name='peliculas'),
    path('movie/<pk>', movie, name="movie"),
    path('login/', login, name='login'),
]