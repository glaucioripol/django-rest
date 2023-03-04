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
