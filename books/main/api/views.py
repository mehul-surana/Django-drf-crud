from rest_framework import viewsets
from main.models import Book
from .serializer import BookSerializer
class BookViewSets(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



