from django.urls import path, include
from fbv_app import views

from rest_framework.routers import DefaultRouter

# * viewsets
router = DefaultRouter()
router.register(
    '',
    views.StudentViewSet
)

urlpatterns = [
    # * function based views
    path('students/function/', views.student),
    path('students/function/<str:pk>', views.student_by_id),

    # * class based views
    path('students/class/', views.StudentAPIView.as_view()),
    path('students/class/<str:pk>/', views.StudentDetails.as_view()),

    # * class based views with mixins
    path('students/mixins/', views.StudentListWithMixin.as_view()),
    path('students/mixins/<str:pk>/', views.StudentsDetailsWithMixin.as_view()),

    # * class based views with generics
    path('students/generics/', views.StudentListGeneric.as_view()),
    path(
        'students/generics/<str:pk>/',
        views.StudentDetailsGeneric.as_view()
    ),

    # * ModelViewSet
    path('students/model_viewsets/', include(router.urls))
]
