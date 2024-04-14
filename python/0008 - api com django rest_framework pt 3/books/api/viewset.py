from rest_framework import viewsets
from books.api import serializers
from books import models

from rest_framework.permissions import IsAuthenticated


class BooksViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.BookSerializer
    queryset = models.Books.objects.all()
