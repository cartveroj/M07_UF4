from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context , loader
from django.shortcuts import render
# Create your views here.

#variables globales
teachers = [
        {
        "id":"1",
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
            "id":"2",
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
            "id":"3",
            "name":"Josep Oriol",
            "surname_1":"Roca",
            "surname_2":"Fabra",
            "email": "oriol@iticbcn.cat",
            "course": "2024",
            "tutor": "si",
            "modules":"M09",
            "rol":"teacher"
        },{
            "id":"4",
            "name":"Xavi",
            "surname_1":"Quesada",
            "surname_2":"Puertas",
            "email": "xavi@iticbcn.cat",
            "course": "2024",
            "tutor": "no",
            "modules":"M08",
            "rol":"teacher"
        }]
students = [
        {
        "id":"1",
        "name":"Joana",
        "surname_1":"Li",
        "surname_2":"Chen",
        "age":"24",
        "email": "joana_li@iticbcn.cat",
        "course": "DAW2A",
        "modules":"M07,M08,M09",
        "rol":"student"
        },
        {
        "id":"2",
        "name":"Oriana",
        "surname_1":"Rojas",
        "surname_2":"Guedez",
        "age":"24",
        "email": "oriana@iticbcn.cat",
        "course": "DAW2A",
        "modules":"M07,M09,M08,M06",
        "rol":"student"
        },
         {
        "id":"3",
        "name":"Veronica",
        "surname_1":"Cartagena",
        "surname_2":"Jaldin",
        "age":"30",
        "email": "veronica@iticbcn.cat",
        "course": "DAW2A",
        "modules":"M07,M08,M09,M06",
        "rol":"student"
        }]

#endPoint que retorna una vista de bienvenida
def welcome(request):
    return render(request,'index_centre.html')

#endPoint que va hacia la vista de teachers con el un objeto que contiene los datos de teachers
def teacher(request):

    return render(request,'index_teachers.html',{'data':teachers})

#endPoint que va hacia la vista de stdudents con el un objeto que contiene los datos de students
def student(request):
    
    return render(request,'index_students.html',{'data':students})
#recibe por parametro la id y realiza el filtro y envia el objeto que coincide
def teacherInfo(request, pk):
    teacher_obj = None
    for i in teachers:
        if i['id'] == pk:
            teacher_obj = i
    return render(request,'teacher.html',{'teacher':teacher_obj})

#recibe por parametro la id y realiza el filtro y envia el objeto que coincide
def studentInfo(request, pk ):
    student_obj = None
    for i in students:
        if i['id'] == pk:
            student_obj = i
    return render(request,'student.html',{'student':student_obj})