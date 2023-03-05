from django.db.models import Model
from django.db import models

from datetime import datetime

# Create your models here.


class Flight(Model):
    id = models.AutoField(primary_key=True)
    flight_number = models.IntegerField()
    operating_airline = models.CharField(max_length=20)
    departure_city = models.CharField(max_length=20)
    arrival_city = models.CharField(max_length=20)
    date_of_departure = models.DateField()
    estimated_time_of_departure = models.TimeField()

    def __str__(self):
        return f"{self.id} - {self.flight_number} - {self.operating_airline} - {self.departure_city} - {self.arrival_city} - {self.date_of_departure} - {self.estimated_time_of_departure}"


class Passenger(Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id} - {self.first_name} - {self.last_name} - {self.middle_name} - {self.email} - {self.phone}"


class Reservation(Model):
    id = models.AutoField(primary_key=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.flight} - {self.passenger}"
