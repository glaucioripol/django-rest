from rest_framework.serializers import ModelSerializer

from flight_app.models import Flight, Passenger, Reservation


class FlightSerializer(ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class PassengerSerializer(ModelSerializer):
    reservations = ReservationSerializer(many=True, read_only=True)

    class Meta:
        model = Passenger
        fields = '__all__'
