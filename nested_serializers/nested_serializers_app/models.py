from django.db.models import Model
from django.db import models

# Create your models here.


class Author(Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} - {self.first_name} {self.last_name}'


class Book(Model):
    title = models.CharField(max_length=100)
    ratings = models.CharField(max_length=20, blank=True, null=True)
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
