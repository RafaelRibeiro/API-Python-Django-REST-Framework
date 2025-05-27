# API TODO com Django REST Framework

API simples para gerenciamento de tarefas (TODO), construída com Django e Django REST Framework.

---

## Descrição

Esta aplicação permite criar, listar, atualizar e deletar tarefas (todos) via API RESTful. Cada tarefa possui:

- Nome (API TODO com Django REST Framework)
- Status (Concluido)
- Data de criação (2025-05-27 15:00:00)

---

## Tecnologias usadas

- Python 3.10
- Django 5.2.1
- Django REST Framework 3.14.0
- SQLite (banco de dados padrão para desenvolvimento)

---

## Estrutura do Projeto

- `app/`: Aplicação principal contendo modelos, views, serializers e URLs.
- `api_todo/`: Configurações do projeto Django e URLs globais.
- `db.sqlite3`: Banco de dados SQLite local.
- `manage.py`: Script para executar comandos Django.

---

## Como rodar a aplicação localmente

### Pré-requisitos

- Python 3.10 instalado
- Ambiente virtual (recomendado)

### Passos

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd api_todo
