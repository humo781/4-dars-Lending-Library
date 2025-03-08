from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'bio', 'birth_date', 'nationality')
    list_filter = ('first_name', 'last_name', 'birth_date', 'nationality')

