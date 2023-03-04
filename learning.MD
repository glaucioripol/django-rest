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
