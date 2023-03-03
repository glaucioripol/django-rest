from django.db.models import Model
from django.db import models

from json import dumps as json

# Create your models here.


class Employee(Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return json({
            'id': self.id,
            'name': self.name,
            'salary': self.salary,
        })

    def __str__(self):
        return self.name
