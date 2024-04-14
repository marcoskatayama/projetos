# Tutorial: Criando uma API REST com Django REST Framework

Este é um tutorial passo a passo para criar uma API REST do zero usando Django REST Framework. Vamos criar uma API para gerenciar uma biblioteca de livros.

Fonte [COMO CRIAR UMA API REST DO ZERO COM DJANGO REST FRAMEWORK](https://www.youtube.com/watch?v=wtl8ZyCbTbg&list=PLcM_74VFgRhpyCtsNXyBUf27ZRbyQnEEb&index=1)

## Pré-requisitos

- Python 3 instalado
- Ambiente virtual ativado

## 1. Configurando o Projeto

Vamos criar e ativar o ambiente virtual

```bash
python -m venv venv

.\venv\Scripts\activate
```

## 2 Instalação

```bash
pip install djangorestframework
```

Vamos criar o projeto, o ponto depois do library indica para o django criar no diretorio atual

```bash
django-admin startproject library .
```

Adicionar o modulo

```bash
django-admin startapp books
```

Gerar migrate 

* precisa estar com o amnbiente virtual desativado: `deactivate`

```bash
python manage.py migrate
```

No arquivo settings.py:

```python
INSTALLED_APPS = [
    # lib
    'rest_framework',

    # app
    'books'
]
```

## 3 Models

No arquivo models do books

```bash
from django.db import models
from uuid import uuid4

class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)

```

## 4 Serializers e views

Dentro da pasta books vamos criar pasta api e dentro criar os arquivos serializers.py e viewset.py

```python
from rest_framework import serializers
from books import models


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Books
        fields = '__all__'

```

```python
from rest_framework import viewsets
from books.api import serializers
from books import models


class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookSerializer
    queryset = models.Books.objects.all()

```

## 5 Rotas

Vamos adicionar a rota no arquivo urls do libray

```python
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from books.api import viewset as booksviewsets

route = routers.DefaultRouter()

route.register(r'books', booksviewsets.BooksViewSet, basename='Books')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
```

Como foi adicionado o model books, vamos adicionar na migration

```bash
python manage.py makemigrations
python manage.py migrate
```

## 6 Executar o projeto

```bash
python manage.py runserver
```