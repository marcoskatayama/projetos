# Tutorial: Adicionando autenticação JWT

Fonte [COMO INCLUIR AUTENTICAÇÃO JWT EM API REST - DJANGO REST FRAMEWORK + TOKEN JWT](https://www.youtube.com/watch?v=LFV4MLe0ZzM&list=PLcM_74VFgRhpyCtsNXyBUf27ZRbyQnEEb&index=11).

## 1. Instalação

```bash
pip install djangorestframework-simplejwt
```

## 2. Settings

Vamos adicionar

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
```

## 3. Urls

Vamos adicionar 

```python
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

path('token/', TokenObtainPairView.as_view()),
path('token/refresh/', TokenRefreshView.as_view()),
```

resultado final

```python
"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from rest_framework import routers

from books.api import viewset as booksviewsets

route = routers.DefaultRouter()

route.register(r'books', booksviewsets.BooksViewSet, basename='Books')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('', include(route.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

## 4. Adicionado autenticação nas rotas

Na view que queremos que tenha autenticação vamos adicionar 

```python
from rest_framework.permissions import IsAuthenticated


class BooksViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
```

resultado final

```python
from rest_framework import viewsets
from books.api import serializers
from books import models

from rest_framework.permissions import IsAuthenticated


class BooksViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.BookSerializer
    queryset = models.Books.objects.all()

```

Ao tentar acessar agora a rota http://127.0.0.1:8000/books/

terá o retorno 

```json
{
    "detail": "Authentication credentials were not provided."
}
```

## 5. Criar superusuario

```bash
python manage.py createsuperuser
```

## 6. Rodar o servidor

Após criar o usuario vamos enviar requisição POST para rota http://127.0.0.1:8000/token/

passando no body:

```json
{
    "username" : "usuairio",
    "password" : senha
}
```

Será retornando o access que é o token

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMzIxOTc4NywiaWF0IjoxNzEzMTMzMzg3LCJqdGkiOiI3YzQwOWM4ZjhlZjU0NTdlYjUwNTI3NmI1ZTRhZWQyMiIsInVzZXJfaWQiOjF9.gQkjhI2IV0QAKk_NKoo8E15c64Gv4plcnSyi_XaMPaw",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzMTMzNjg3LCJpYXQiOjE3MTMxMzMzODcsImp0aSI6IjBlNDcxODBkODkyOTRiMGE5YzQxYWIyMGNiYzMzOGViIiwidXNlcl9pZCI6MX0.j11aTCnLygaegvSlGSZfvEn8jUpwzMPq2daMA8PkLB4"
}
```

Agora ao tentar acessar a rota http://127.0.0.1:8000/books/ via get passando no authorization Bearer + token, será retornado o conteudo.

## 7. Refresh token

Para conseguir um novo token, podemos usar a rota token/refresh/ via post passando no body

Este refresh tem um tempo maior para expiração que o token geralmente 24h

```json
{
    "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMzIxOTc4NywiaWF0IjoxNzEzMTMzMzg3LCJqdGkiOiI3YzQwOWM4ZjhlZjU0NTdlYjUwNTI3NmI1ZTRhZWQyMiIsInVzZXJfaWQiOjF9.gQkjhI2IV0QAKk_NKoo8E15c64Gv4plcnSyi_XaMPaw"
}
```

Será retornado um novo token

```json
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzMTM0NTk0LCJpYXQiOjE3MTMxMzM4NTcsImp0aSI6ImE4NTdhM2FjZTJkZTRhODQ4YmM4MzNmZjNlMzE1YzhkIiwidXNlcl9pZCI6MX0.XDHlCnrjLas80FurzmIZhJAnwPqAkJ9t8fMD8sAwGB4"
}
```