from rest_framework import generics
from .serializers import AuthorSerializer
from .pagination import AuthorPagination
from .models import Author

class AuthorListCreateApiView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorPagination
