from django.contrib import admin  #Painel administrativo do Django
from django.urls import path, include  #Rotas e inclusão de URLs
from rest_framework.routers import DefaultRouter  #Router para os ViewSets
from filmes.views import GenerosViewSet, FilmesViewSet  #ViewSets registrados no router
from rest_framework.authtoken.views import obtain_auth_token  #Autenticação por token

router = DefaultRouter()
router.register(r'generos', GenerosViewSet)  #Endpoint para gêneros: /api/generos/
router.register(r'filmes', FilmesViewSet)  #Endpoint para filmes: /api/filmes/

urlpatterns = [
    path('admin/', admin.site.urls),  #Painel administrativo
    path('api/', include(router.urls)),  #Rotas da API
    path('api/token/', obtain_auth_token),  #Obtenção do token
]
