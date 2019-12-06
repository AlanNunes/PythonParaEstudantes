from django.contrib import admin

# Register your models here.
from .models import Generos, Filmes

admin.site.register(Generos)
admin.site.register(Filmes)
