from app.models import Todo            # Importa o modelo Todo para ser serializado
from rest_framework import serializers # Importa o módulo serializers do Django REST Framework para criação dos serializers

# Serializer para o modelo Todo, responsável por converter objetos Todo para JSON e vice-versa
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo                                   # Define o modelo que será serializado
        fields = ['id', 'name', 'done', 'created_at']  # Define os campos do modelo que serão incluídos na serialização
