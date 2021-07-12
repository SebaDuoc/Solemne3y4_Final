from django.shortcuts import render
from django.http import request
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

#listado de peliculas
def views_movie(request):
    peliculas = Movie.objects.all()
    datos = {
        'peliculas' : peliculas
    }
    return render(request, 'core/views_movie.html', datos)

#formularo para crear una pelicula
def add_movie(request):
    datos = {
        'form': MovieForm() 
        }
    if request.method == 'POST':
        formulario_add = MovieForm(request.POST)
        if formulario_add.is_valid:
            formulario_add.save()
            datos['mensaje'] = "Pelicula agregada perfectamente a los archivos"

    return render(request, 'core/add_movie.html', datos)

    #formulario para editar pelicula
def edit_movie(request, pk):
    movie = Movie.objects.get(cCodigo=pk)
    datos = {
        'form': MovieForm(instance=movie)
    }
    if request.method == 'POST':
        formulario_edit = MovieForm(data=request.POST, instance=movie)
        if formulario_edit.is_valid:
            formulario_edit.save()
            datos['mensaje'] = "Pelicula editada correctamente"
    return render(request, 'core/edit_movie.html', datos)