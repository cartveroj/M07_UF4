from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context , loader
from django.shortcuts import render
# Create your views here.

def index(request):
    profesor = {"name":"Roger", "surname":"Sobrino"}
    # template = loader.get_template('index.html')
    # dades = template.render({'nombre':profesor["name"]})
    return render(request,'index.html',{'nombre':profesor["name"],'surname':profesor["surname"]})

def teacher(request):
    teachers = [
        {
        "name":"Roger",
        "surname_1":"Sobrino",
        "surname_2":"Caceres",
        "email": "roger@iticbcn.cat",
        "course": "2024",
        "tutor": "si",
        "modules":"M07"
        },
        {
            "name":"Juanma",
            "surname_1":"Sobrino",
            "surname_2":"Caceres",
            "email": "roger@iticbcn.cat",
            "course": "2024",
            "tutor": "si",
            "modules":"M07"
        }]
    return render(request,'index_teachers.html',{'data':teachers})

def student(request):
    students = [
        {
        "name":"Roger",
        "surname_1":"Sobrino",
        "surname_2":"Caceres",
        "email": "roger@iticbcn.cat",
        "course": "2024",
        "tutor": "si",
        "modules":"M07"
        },
        {
            "name":"Juanma",
            "surname_1":"Sobrino",
            "surname_2":"Caceres",
            "email": "roger@iticbcn.cat",
            "course": "2024",
            "tutor": "si",
            "modules":"M07"
        }]
    return render(request,'index_students.html',{'data':students})