from django.db import models

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id categoria")
    nombreCategoria = models.CharField(max_length=50, verbose_name="Nombre categoria")

    def __str__(self):
        return self.nombreCategoria

class Movie(models.Model):
    cPelicula = models.AutoField(primary_key = True, verbose_name="Codigo de Pelicula")
    Nombre = models.CharField(max_length=20, verbose_name="Nombre" )
    País = models.CharField(max_length=20, null=True, blank=True, verbose_name="País")
    año = models.CharField(max_length=20, null=True, blank=True, verbose_name="Año")
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.cPelicula
