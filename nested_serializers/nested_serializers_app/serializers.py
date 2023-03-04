from rest_framework.serializers import ModelSerializer

from .models import Author, Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(ModelSerializer):
    # * This is the magic line that makes the nested serialization work
    # * shows all the books for the author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = '__all__'
