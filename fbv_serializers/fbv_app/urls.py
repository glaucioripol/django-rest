from django.urls import path
import fbv_app.views as views

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
]
