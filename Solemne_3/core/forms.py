from django import forms
from django.forms import ModelForm
from .models import Movie

#formulario para crear (y editar) peliculas
class MovieForm(ModelForm):

    class Meta:
        model = Movie
        fields = ['cPelicula','nombre','país','año','categoria']