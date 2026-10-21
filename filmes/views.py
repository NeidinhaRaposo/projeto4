from rest_framework import viewsets  #ViewSets do DRF para CRUD automático
from .models import Generos, Filmes  #Modelos/tabelas usados nas views
from .serializers import GenerosSerializer, FilmesSerializer  #Serializers dos modelos
from django_filters.rest_framework import DjangoFilterBackend  #Permite filtragem via query params


#ViewSet para o modelo Generos, fornece endpoints CRUD
class GenerosViewSet(viewsets.ModelViewSet):
    queryset = Generos.objects.all()  #Queryset base usado pelo ViewSet
    serializer_class = GenerosSerializer  #Serializer do modelo Generos


#ViewSet para o modelo Filmes, fornece endpoints CRUD e suporte a filtros
class FilmesViewSet(viewsets.ModelViewSet):
    queryset = Filmes.objects.all()  #Queryset base para operações do ViewSet
    serializer_class = FilmesSerializer  #Serializer usado para filmes
    filter_backends = [DjangoFilterBackend]  #Habilita filtragem via django-filter
    #Campos permitidos para filtragem via query string
    filterset_fields = ['titulo', 'genero__nome', 'ano_lancamento', 'duracao']
