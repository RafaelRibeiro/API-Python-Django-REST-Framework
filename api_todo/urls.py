"""
URL configuration for api_todo project.

This file defines the URL routes for the entire project.

Django processes URLs in the order they appear here, 
routing requests to the appropriate view or included URL config.
"""

from django.contrib import admin      # Importa o painel administrativo do Django
from django.urls import include, path # Importa as funções 'include' e 'path' para definir rotas e incluir outras URLs


# Lista principal de URLs do projeto
urlpatterns = [
    # Rota para acessar a interface administrativa padrão do Django
    path('admin/', admin.site.urls),
    
    # Inclui as URLs definidas no arquivo 'app.urls' dentro do caminho '/todo/'
    # Ou seja, todas as rotas definidas no app estarão disponíveis a partir de /todo/
    path('todo/', include('app.urls')),  
]
