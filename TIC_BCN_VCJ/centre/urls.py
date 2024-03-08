from django.urls import path

from . import views
#view.teacher es el nombre de las funciones
urlpatterns = [
    path('', views.index, name='index'),
    path('prof', views.teacher, name='profesor'),
    path('alum', views.student, name='alumnes'),

]