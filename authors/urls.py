from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.AuthorListCreateApiView.as_view(), name='list-create')
]
