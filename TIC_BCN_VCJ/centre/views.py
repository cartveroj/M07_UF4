from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context , loader
from django.shortcuts import render
# Create your views here.

def teacher(request):
    teachers = [
        {
        "name":"Roger",
        "surname_1":"Sobrino",
        "surname_2":"Caceres",
        "email": "roger@iticbcn.cat",
        "course": "2024",
        "tutor": "si",
        "modules":"M07",
        "rol":"teacher"
        },
        {
            "name":"Juan Manuel",
            "surname_1":"Sanchez",
            "surname_2":"Bel",
            "email": "juanma@iticbcn.cat",
            "course": "2024",
            "tutor": "si",
            "modules":"M06",
            "rol":"teacher"
        },
        {
            "name":"Josep Oriol",
            "surname_1":"Roca",
            "surname_2":"Fabra",
            "email": "oriol@iticbcn.cat",
            "course": "2024",
            "tutor": "si",
            "modules":"M09",
            "rol":"teacher"
        },{
            "name":"Xavi",
            "surname_1":"Quesada",
            "surname_2":"Puertas",
            "email": "xavi@iticbcn.cat",
            "course": "2024",
            "tutor": "no",
            "modules":"M08",
            "rol":"teacher"
        }]
    return render(request,'index_teachers.html',{'data':teachers})

def student(request):
    students = [
        {
        "name":"Joana",
        "surname_1":"Li",
        "surname_2":"Chen",
        "age":"24",
        "email": "joana_li@iticbcn.cat",
        "course": "DAW2A",
        "modules":"M07,M08,M09"
        },
        {
            "name":"Oriana",
            "surname_1":"Rojas",
            "surname_2":"Guedez",
            "age":"24",
            "email": "oriana@iticbcn.cat",
            "course": "DAW2A",
            "modules":"M07,M09,M08,M06"
        },
         {
        "name":"Veronica",
        "surname_1":"Cartagena",
        "surname_2":"Jaldin",
        "age":"30",
        "email": "veronica@iticbcn.cat",
        "course": "DAW2A",
        "modules":"M07,M08,M09,M06"
        }]
    return render(request,'index_students.html',{'data':students})