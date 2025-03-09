from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListCreateAPiView.as_view(), name='list-create'),
    # path('authors/<int:pk>/', views.AuthorDetailApiView.as_view(), name='detail'),
    # path('authors/<int:pk>/books/', views.AuthorBookApiView.as_view(), name='author-books'),
]
