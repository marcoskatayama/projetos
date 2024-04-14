# Tutorial: Adicionando upload de imagens

Fonte [COMO FAZER UPLOAD DE IMAGENS EM API REST COM DJANGO REST FRAMEWORK](https://www.youtube.com/watch?v=Syoz9ldmS6o&list=PLcM_74VFgRhpyCtsNXyBUf27ZRbyQnEEb&index=3).

## Pré-requisitos

- Python 3 instalado

## 1. Instalação

Vamos adicionar uma biblioteca que gerencia as imagens no python

```bash
pip install pillow
```

## 2. Models

Vamos adicionar coluna image 

```python
from django.db import models
from uuid import uuid4


def upload_image_book(isnstance, filename):
    return f"{isnstance.id_book}-{filename}"


class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)
    image = models.ImageField(
        upload_to=upload_image_book,
        blank=True,
        null=True
        )

```

```bash
python manage.py makemigrations

python manage.py migrate
```

## 3. Settings

Vamos importar os

```python
import os
```

e adicionar 

```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

## 4. Urls

vamos importar 

```python
from django.conf import settings
from django.conf.urls.static import static
```

e adicionar

```python
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

resultado final

```python
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers

from books.api import viewset as booksviewsets

route = routers.DefaultRouter()

route.register(r'books', booksviewsets.BooksViewSet, basename='Books')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 5. Executar o projeto

```bash
python manage.py runserver
```
