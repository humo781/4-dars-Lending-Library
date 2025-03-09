from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AuthorSerializer
from .models import Author
from books.serializers import BookSerializer

class AuthorListCreateApiView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorBookApiView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        author = get_object_or_404(Author, pk=self.kwargs['pk'])
        return author.books.all()
