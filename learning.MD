# Learning path

## How to generate a new django project

```bash
django-admin startproject <project-name>
```

## Create a new app

i can create many apps in a project

```bash
python manage.py startapp <app-name>
```

## migrations

### Create migrations

```bash
python manage.py makemigrations
```

### Apply migrations

```bash
python manage.py migrate
```

## Create superuser

```bash
python manage.py createsuperuser
```

## filter which columns use in a model

```python
class Meta:
    fields = ['name', 'email']
```

## default pagination

put this in settings.py

```python
# * Pagination default - it will be used for all the views
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

## filter

install `django-filter`

```bash
pip install django-filter
```

add `django_filters` to `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    ...
    'django_filters',
]
```

defining as global

```python
# * Pagination default - it will be used for all the views
REST_FRAMEWORK = {
    ...
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
```

## defining all routes should access just for authenticated users

```python
REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        ...
    ]
}
```

## defining all routes should access just for authenticated users and django admin permission

```python
REST_FRAMEWORK = {
    ...
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.DjangoModelPermissions',
        'rest_framework.permissions.<permission-name>'
    ]
}
```

## Validate data in serializer

```python
from rest_framework import serializers
class FlightSerializer(ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

    def validate_flight_number(self, flight_number: int):
        if (match(r'^\d$', str(flight_number)) == None):
            raise serializers.ValidationError(
                'Flight number must be a number'
            )

        return flight_number
    # * field per field
    def validate_<field_name>(self, <field_name>):
        if (<field_name> == None):
            raise serializers.ValidationError(
                '<field_name> must be a number'
            )

        return <field_name>

    # * all fields
    def validate(self, data):
        if (data['<field_name_in_your_model>'] == data['<field_name_in_your_model>']):
            raise serializers.ValidationError(
                'Flight number must be a number'
            )

        return data
```

with `validators`

```python
from django.core.validators import RegexValidator
class FlightSerializer(ModelSerializer):
    flight_number = serializers.CharField(
        validators=[
            RegexValidator(
                regex=r'^\d+$',
                message='Flight number must be a number'
            )
        ]
    )
```

with `validators` and `fields`

```python
from django.core.validators import RegexValidator
class FlightSerializer(ModelSerializer):
    flight_number = serializers.CharField(
        validators=[
            RegexValidator(
                regex=r'^\d+$',
                message='Flight number must be a number'
            )
        ],
        fields='__all__'
    )
```

with array of `validators`

```python
def validate_flight_data(data: dict):
    flight_number = data['flight_number']
    if (match(r'^\d$', str(flight_number)) == None):
        raise serializers.ValidationError(
            'Flight number must be a number'
        )

    return flight_number

class FlightSerializer(ModelSerializer):

    arrival_city = serializers.CharField(
        max_length=20,
        error_messages={
            'required': 'Arrival city is required',
            'max_length': 'Arrival city must be less than 20 characters'
        }
    )

    class Meta:
        model = Flight
        fields = '__all__'
        validators = [
            validate_flight_data,
        ]
```

## How to put authentication by token

```python

# setings.py

INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    ...
]

REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

```

in the request header i should put this header `Authorization: Token <token>`

and token is saved on table `authtoken_token`

## configuring CORS

install `django-cors-headers`

```bash
pip install django-cors-headers
```

add `corsheaders` to `INSTALLED_APPS`

```python
# settings.py

INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]

MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    ...
]

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

or 
ALLOWED_HOSTS = []
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST=[
    # * put the url of your frontend
    'http://localhost:3000',
]
```
