from rest_framework.serializers import ModelSerializer

from fbv_app.models import Student


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'score']
