from rest_framework import serializers  #Ferramentas do DRF para transformar a tabela em JSON
from .models import Generos, Filmes  #Modelos usados pelos serializers

class GenerosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generos
        fields = '__all__'  #Expõe todos os campos do modelo Generos

class FilmesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filmes
        fields = '__all__'  #Expõe todos os campos do modelo Filmes
