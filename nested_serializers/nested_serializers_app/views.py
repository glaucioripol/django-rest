from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from .pagination import AuthorPagination, BookPagination


# Create your views here.
class AuthorListView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorPagination
    # * using django_filters, util for filtering per fields
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['first_name', 'last_name']

    # * using rest_framework filters
    filter_backends = [SearchFilter, OrderingFilter]
    # * prefix in fields and your function will be called
    # * "<field_name>" - contains
    # * "ˆ<field_name>" - starts with
    # * "=<field_name>" - exact match
    # * "@<field_name>" - full text search(Currently only supported Django's PostgreSQL backend.)
    search_fields = ['first_name', 'last_name']

    # * ordering, filter by fields
    ordering_fields = ['first_name', 'last_name']


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
