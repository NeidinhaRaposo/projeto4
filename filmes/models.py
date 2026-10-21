from django.db import models

class Generos(models.Model):
    nome = models.CharField(max_length=255)  #Nome do gênero

    def __str__(self):
        return self.nome  #Representação em string do gênero

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'

class Filmes(models.Model):
    titulo = models.CharField(max_length=255)  #Título do filme
    descricao = models.TextField()  #Descrição do filme
    ano_lancamento = models.PositiveIntegerField()  #Ano de lançamento
    genero = models.ForeignKey(Generos, on_delete=models.CASCADE)  #Relacionamento com Generos
    duracao = models.PositiveIntegerField()  #Duração em minutos

    def __str__(self):
        return self.titulo  #Representação em string do filme

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'