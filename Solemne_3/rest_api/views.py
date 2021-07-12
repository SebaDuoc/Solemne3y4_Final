from django.shortcuts import render
from .serializers import MovieSerializer
from core.models import Movie
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def peliculas(request):
    """
    Lista todos los peliculas
    """
    if request.method == 'GET':
        peliculas_lista = Movie.objects.all()
        serializer = MovieSerializer(peliculas_lista, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        """
        Agrega una pelicula
        """
        data = JSONParser().parse(request)
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
@permission_classes((IsAuthenticated,))
def movie(request, pk):
    try:
        movie = Movie.objects.get(patente=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    """
    GET: Muestra detalles de una pelicula segun cPelicula

    """
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        """
        PUT: Edita una pelicula segun cPelicula
        """
        data = JSONParser().parse(request)
        serializer = MovieSerializer(movie, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
