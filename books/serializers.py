from rest_framework import serializers
from authors.models import Author
from .models import Book, Genre
from authors.serializers import ShortAuthorSerializer, AuthorSerializer

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    isbn = serializers.CharField()
    published_at = serializers.DateField()
    copies_available = serializers.SerializerMethodField()

    def get_copies_available(self, obj):
        return obj.bookCopy.count()

class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

class BookListCreateSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=Author.objects.all())
    genre_1 = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Genre.objects.all())
    authors_display = serializers.SerializerMethodField()
    genre = GenreSerializer(read_only=True)
    copies_available = serializers.SerializerMethodField()

    def get_copies_available(self, obj):
        return obj.bookCopy.count()

    def get_authors_display(self, obj):
        return ShortAuthorSerializer(obj.authors.all(), many=True).data

    class Meta:
        model = Book
        fields = ['id', 'title', 'authors_display', 'authors', 'genre', 'genre_1', 'isbn', 'published_at', 'description',
                  'page_count', 'language', 'copies_available']
