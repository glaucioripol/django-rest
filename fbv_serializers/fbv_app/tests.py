from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer
from .views import student, StudentDetails


class StudentViewTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.student_data = {
            'name': 'John Doe',
            'score': '10.000'
        }

    def test_get_students(self):

        data_mocked = {'name': 'Alice', 'score': '30.000'}
        # cria um estudante para testar
        Student.objects.create(**data_mocked)

        # faz uma solicitação GET à view
        request = self.factory.get('/students/function/')
        response = student(request)

        # verifica se o status da resposta é 200 OK
        self.assertEqual(response.status_code, 200)

        converted_list = [dict(item) for item in response.data]

        # verifica se a resposta contém os dados do estudante criado
        data_expected = {
            'id': converted_list[0]['id'],
            'name': data_mocked['name'],
            'score': data_mocked['score']
        }

        self.assertEqual(converted_list, [data_expected])

    def test_create_student(self):
        # faz uma solicitação POST à view com dados de estudante
        request = self.factory.post(
            '/students/function/',
            data=self.student_data
        )

        response = student(request)

        # verifica se o status da resposta é 201 Created
        self.assertEqual(response.status_code, 201)

        # verifica se o estudante foi criado no banco de dados
        self.assertEqual(Student.objects.count(), 1)

        # verifica se os dados do estudante criado são os mesmos que foram enviados na solicitação
        student_data = Student.objects.first()

        data_serialized = StudentSerializer(student_data).data

        expected_data = {
            'id': data_serialized['id'],
            'name': self.student_data['name'],
            'score': self.student_data['score']
        }

        self.assertEqual(
            data_serialized,
            expected_data
        )


class StudentDetailsTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.student1 = Student.objects.create(name="John Doe", score='90.000')
        self.student2 = Student.objects.create(name="Jane Doe", score='80.000')

    def test_get_valid_student(self):
        student_1_serialized = StudentSerializer(self.student1).data

        student_1_id = student_1_serialized['id']

        request = self.factory.get(
            f'/students/class/{student_1_id}/')
        response = StudentDetails.as_view()(request, pk=student_1_id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = StudentSerializer(self.student1).data
        self.assertEqual(response.data, expected_data)

    def test_get_invalid_student(self):
        uuid = '4e3c9b0c-0b1c-4b9c-9c1c-4b9c9b0c9b0c'
        request = self.factory.get(f'/students/class/{uuid}/')
        response = StudentDetails.as_view()(request, pk=uuid)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_valid_student(self):
        new_data = {'name': 'John Smith', 'score': '95.000'}
        student_1_serialized = StudentSerializer(self.student1).data
        current_student_id = student_1_serialized['id']

        request = self.factory.put(
            f'/students/class/{current_student_id}/',
            data=new_data,
            format='json'
        )

        response = StudentDetails.as_view()(request, pk=current_student_id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_student = Student.objects.get(id=self.student1.id)

        updated_student_serialized = StudentSerializer(updated_student).data

        self.assertEqual(updated_student_serialized['name'], new_data['name'])
        self.assertEqual(
            updated_student_serialized['score'],
            new_data['score']
        )

    def test_put_invalid_student(self):
        uuid = '4e3c9b0c-0b1c-4b9c-9c1c-4b9c9b0c9b0c'

        new_data = {'name': 'John Smith', 'score': '99.000', 'id': uuid}

        request = self.factory.put(
            f'/students/class/{uuid}/',
            data=new_data,
            format='json'
        )

        response = StudentDetails.as_view()(request, pk=uuid)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Student.objects.get(
            id=self.student1.id).name, self.student1.name)

    def test_delete_valid_student(self):
        student_1_serialized = StudentSerializer(self.student1).data
        current_student_id = student_1_serialized['id']
        request = self.factory.delete(
            f'/students/class/{current_student_id}/')
        response = StudentDetails.as_view()(request, pk=current_student_id)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Student.objects.filter(id=self.student1.id).exists())

    def test_delete_invalid_student(self):
        uuid = '4e3c9b0c-0b1c-4b9c-9c1c-4b9c9b0c9b0c'
        request = self.factory.delete(f'/students/class/{uuid}/')
        response = StudentDetails.as_view()(request, pk=uuid)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
