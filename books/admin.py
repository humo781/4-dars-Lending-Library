from django.contrib import admin
from . import models

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name', 'description')

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'isbn', 'published_at', 'language', 'page_count')
    list_filter = ('title', 'isbn', 'page_count')

@admin.register(models.BookCopy)
class BookCopyAdmin(admin.ModelAdmin):
    list_display = ('book', 'inventory_number', 'condition', 'added_date')

@admin.register(models.BookLending)
class BookLendingAdmin(admin.ModelAdmin):
    list_display = ('book_copy', 'borrower_name', 'borrower_email', 'borrowed_date', 'status')
    list_filter = ('borrower_name', 'borrowed_date')
