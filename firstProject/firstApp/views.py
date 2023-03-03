from django.shortcuts import render
from django.http import HttpRequest, JsonResponse

from .models import Employee


def employee(request: HttpRequest):

    # specify the columns with values() method
    data = Employee.objects.all()

    response = {
        'records': list(data.values('id', 'name', 'salary'))
    }

    return JsonResponse(response)
