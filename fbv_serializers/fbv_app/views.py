from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.http import HttpRequest

from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.viewsets import ModelViewSet


from .models import Student
from .serializers import StudentSerializer

# Create your views here.

# * function based views - very good to simple logic


@api_view(['GET', 'POST'])
def student(request):

    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_by_id(request: HttpRequest, pk: str):

    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# * class based views - very good to business logic
class StudentAPIView(APIView):

    def get(self, _: HttpRequest):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)

        return Response(serializer.data)

    def post(self, request: HttpRequest):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetails(APIView):

    def get(self, _: HttpRequest, pk: str):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)

        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request: HttpRequest, pk: str):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, _: HttpRequest, pk: str):
        try:
            Student.objects.get(pk=pk).delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


# * class based views with mixins - very good to simple CRUD

class StudentListWithMixin(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request: HttpRequest) -> Response:
        return self.list(request)

    def post(self, request: HttpRequest) -> Response:
        return self.create(request)


class StudentsDetailsWithMixin(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request: HttpRequest, pk: str) -> Response:
        return self.retrieve(request, pk)

    def put(self, request: HttpRequest, pk: str) -> Response:
        return self.update(request, pk)

    def delete(self, request: HttpRequest, pk: str) -> Response:
        return self.destroy(request, pk)


# * class based views with generics - very good to simple CRUD with less code
class StudentListGeneric(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailsGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# * ModelViewSet - very good to simple CRUD with less code and less code in urls.py
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
