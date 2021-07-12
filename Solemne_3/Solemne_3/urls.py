"""Solemne_3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from core.views import home, views_movie, add_movie, edit_movie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('agregar_movie/', add_movie, name="add_movie" ),
    path('editar_movie/<pk>', edit_movie, name="edit_movie" ),
    path('views_movie/', views_movie, name="views_movie"),
    path('api/', include('rest_api.urls')),
]