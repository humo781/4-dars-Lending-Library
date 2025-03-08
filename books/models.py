from django.db import models
from authors.models import Author

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author, related_name='books')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=100, unique=True)
    published_at = models.DateField(auto_now_add=True)
    description = models.TextField()
    page_count = models.IntegerField()
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class BookCopy(models.Model):
    CONDITION = (
        ('new', 'New'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='bookCopy')
    inventory_number = models.CharField(max_length=100, unique=True)
    condition = models.CharField(max_length=100, choices=CONDITION, default='good')
    is_available = models.BooleanField(default=True)
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Book Copy'
        verbose_name_plural = 'Book Copies'

    def __str__(self):
        return f"{self.book.title} - {self.inventory_number}"

class BookLending(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue'),
    )

    book_copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE, related_name='bookLending')
    borrower_name = models.CharField(max_length=100)
    borrower_email = models.EmailField()
    borrowed_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    returned_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def __str__(self):
        return self.book_copy.book.title
