from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from flight_app.models import Flight, Passenger, Reservation

from re import match

# * Validate the data before saving it to the database


def validate_flight_data(data: dict):
    flight_number = data['flight_number']
    if (match(r'^\d$', str(flight_number)) == None):
        raise serializers.ValidationError(
            'Flight number must be a number'
        )

    return flight_number


class FlightSerializer(ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        validators = [
            validate_flight_data,
        ]

    def validate_flight_number(self, flight_number: int):
        if (match(r'^\d$', str(flight_number)) == None):
            raise serializers.ValidationError(
                'Flight number must be a number'
            )

        return flight_number


class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class PassengerSerializer(ModelSerializer):
    reservations = ReservationSerializer(many=True, read_only=True)

    class Meta:
        model = Passenger
        fields = '__all__'
