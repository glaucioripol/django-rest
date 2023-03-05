from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import AccessToken

from .serializer import (
    UserSerializer,
    UserLoginSerializer,
    UserRequestSerializer,
    UserDTO
)


class Register(APIView):
    def post(self, request: HttpRequest) -> Response:

        user_data = UserRequestSerializer(data=request.data)

        if user_data.is_valid():
            user_to_save = user_data.data
            user_to_save['password'] = make_password(user_to_save['password'])
            user_to_save['is_active'] = True

            user_serialized = UserSerializer(data=user_to_save)

            if user_serialized.is_valid():
                user_serialized.save()

                user_dto = UserDTO(user_serialized.instance)

                token = AccessToken.for_user(user_dto.instance)

                response = {
                    'token': str(token),
                    'user': user_dto.data
                }

                return Response(response, status=status.HTTP_201_CREATED)

            return Response(user_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(user_data.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request: HttpRequest) -> Response:

        user_data = UserLoginSerializer(data=request.data)

        if user_data.is_valid():
            user = user_data.data

            try:
                user_to_login = User.objects.get(email=user['email'])
            except User.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            print(user_to_login.check_password(user['password']))

            if user_to_login.check_password(user['password']):
                token = AccessToken.for_user(user_to_login)

                user_response = UserDTO(user_to_login).data

                response = {
                    'token': str(token),
                    'user': user_response
                }

                return Response(response, status=status.HTTP_200_OK)

            return Response(status=status.HTTP_401_UNAUTHORIZED)

        return Response(user_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_token(request: HttpRequest) -> Response:
    token = AccessToken.for_user(request.user)

    return Response({
        'token': str(token),
        'user': UserDTO(request.user).data
    })
