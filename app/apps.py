from django.apps import AppConfig # Importa a classe base AppConfig do Django para configurar apps

# Classe de configuração do app 'app'
class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' # Define o tipo padrão da chave primária para os modelos deste app como BigAutoField (inteiro grande autoincremental)
    name = 'app'     # Nome do app (deve ser o mesmo nome da pasta do app)