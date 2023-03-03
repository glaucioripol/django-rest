from django.db.models import Model
from django.db import models

from json import dumps as json
from uuid import uuid4


class Student(Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return json({
            'id': self.id,
            'name': self.name,
            'score': self.score,
        })

    def __str__(self):
        return self.name
