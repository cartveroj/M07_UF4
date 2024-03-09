from django.urls import path

from . import views
#view.teacher es el nombre de las funciones
urlpatterns = [
    path('teachers', views.teacher, name='profesor'),
    path('students', views.student, name='alumnes'),
]