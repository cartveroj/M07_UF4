from django.urls import path

from TIC_BCN_VCJ.centre import views

urlpatterns = [
    path('', views.index, name='index'),
]