from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from django_filters.rest_framework import DjangoFilterBackend

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from .pagination import AuthorPagination, BookPagination


# Create your views here.
class AuthorListView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorPagination
    # * This is the magic line that makes the filtering work
    filter_backends = [DjangoFilterBackend]
    # * This is the magic line that makes the filtering per fields
    filterset_fields = ['first_name', 'last_name']


class AuthorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination
    # * This is the magic line that makes the filtering work
    filter_backends = [DjangoFilterBackend]
    # * This is the magic line that makes the filtering per fields
    filterset_fields = ['title', 'author']


class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
