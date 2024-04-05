from django.urls import path

from . import views
#view.teacher es el nombre de las funciones
urlpatterns = [
    #rutas de los endpoints
    path('', views.welcome, name='centre'),

    path('teachers', views.teacher, name='teachers'),
    path('students', views.student, name='students'),

    path('students/student/<str:pk>', views.studentInfo, name='student'),
    path('teachers/teacher/<str:pk>', views.teacherInfo, name='teacher'),

    path('register_user', views.user_form, name='user_form'),

    path('update_user/<str:pk>', views.update_user, name='update_user'),
    path('delete_user/<str:pk>', views.delete_user, name='delete_user'),



]