from rest_framework.serializers import ModelSerializer, ValidationError, Serializer
from rest_framework import serializers

from django.contrib.auth.models import User


class UserRequestSerializer(Serializer):
    username = serializers.CharField(allow_blank=False, min_length=4)
    password = serializers.CharField()
    email = serializers.CharField()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']


class UserDTO(Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.EmailField()


class UserLoginSerializer(Serializer):
    email = serializers.EmailField(allow_blank=False, min_length=4)
    password = serializers.CharField(allow_blank=False, min_length=4)
