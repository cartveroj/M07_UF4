from django.urls import path

from . import views
#view.teacher es el nombre de las funciones
urlpatterns = [
    path('teachers', views.teacher, name='teachers'),
    path('students', views.student, name='students'),

    path('students/student/<str:pk>', views.studentInfo, name='student'),
    path('teachers/teacher/<str:pk>', views.teacherInfo, name='teacher'),
]