from rest_framework import generics
from .serializers import BookListCreateSerializer
from .models import Book

class BookListCreateAPiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListCreateSerializer


# book get, update, delete classini yozish kerak