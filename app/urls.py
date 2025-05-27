from app.views import TodoViewSet                # Importa o ViewSet que define as operações CRUD para o modelo Todo
from rest_framework.routers import DefaultRouter # Importa o roteador padrão do Django REST Framework que gera automaticamente rotas REST

# Cria uma instância do roteador padrão
router = DefaultRouter()

# Registra o TodoViewSet no roteador na raiz ('') do caminho, ou seja, URLs começam com /todo/ (ou o que for configurado no include)
router.register(r'', TodoViewSet)

# O atributo 'urls' do roteador gera automaticamente todas as URLs para as operações CRUD do ViewSet
urlpatterns = router.urls
