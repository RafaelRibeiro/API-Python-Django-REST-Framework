# Importa o módulo models do Django para definir os modelos do banco de dados
from django.db import models

# Modelo Todo representa uma tarefa a fazer
class Todo(models.Model):
    name = models.CharField(max_length=120)              # Campo de texto para o nome da tarefa, limite de 120 caracteres
    done = models.BooleanField(default=False)            # Campo booleano para indicar se a tarefa foi concluída, padrão é False (não concluída)
    created_at = models.DateTimeField(auto_now_add=True) # Data e hora da criação do registro, preenchido automaticamente na criação
