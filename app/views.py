from app.models import Todo                    # Importa o modelo Todo para ser utilizado nas views
from app.serializers import TodoSerializer     # Importa o serializer TodoSerializer para converter dados entre JSON e modelo

from rest_framework import generics            # Importa classes genéricas do Django REST Framework para facilitar criação de views CRUD
from rest_framework import status              # Importa o módulo status para enviar códigos HTTP apropriados nas respostas
from rest_framework import viewsets            # Importa viewsets para facilitar a criação de views baseadas em conjuntos de modelos (ModelViewSet)
from rest_framework.decorators import api_view # Importa decorator para criar views baseadas em funções (não utilizado nas classes abaixo)
from rest_framework.exceptions import NotFound # Importa exceção para retorno quando objeto não é encontrado
from rest_framework.response import Response   # Importa classe para construir respostas HTTP personalizadas
from rest_framework.views import APIView       # Importa classe base para views APIView, para views com lógica customizada (não usada nas classes abaixo)

# ViewSet que oferece todas as operações CRUD para o modelo Todo automaticamente
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()     # Define o conjunto de dados que esta view irá manipular (todos os objetos Todo)
    serializer_class = TodoSerializer # Define o serializer para converter entre JSON e objetos Todo

# View genérica para listar todos os todos e criar um novo todo
class TodoListAndCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()     # Define o conjunto de dados que esta view irá manipular
    serializer_class = TodoSerializer # Define o serializer a ser utilizado

# View genérica para recuperar, atualizar ou deletar um todo específico (por ID)
class TodoDetailChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()     # Define o conjunto de dados que esta view irá manipular
    serializer_class = TodoSerializer # Define o serializer a ser utilizado

