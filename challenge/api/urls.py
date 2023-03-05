from django.urls import path


from . import views

urlpatterns = [
    path('register/', views.Register.as_view()),
    path('login/', views.Login.as_view()),
    path('get_credential/', views.get_token)
]
