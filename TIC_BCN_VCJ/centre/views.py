from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context , loader
from django.shortcuts import render , redirect
from .forms import UserForm #importamos la clase UserForm 
from .models import User
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
  
    teachersData = User.objects.filter(rol='teacher')
    return render(request,'index_teachers.html',{'data':teachersData})

#endPoint que va hacia la vista de stdudents con el un objeto que contiene los datos de students
def student(request):
    
    studentsData = User.objects.filter(rol='student')
    return render(request,'index_students.html',{'data':studentsData})
#recibe por parametro la id y realiza el filtro y envia el objeto que coincide
def teacherInfo(request, pk):
    teacher_obj = User.objects.get(id=pk)
    return render(request,'teacher.html',{'teacher':teacher_obj})

#recibe por parametro la id y realiza el filtro y envia el objeto que coincide
def studentInfo(request, pk ):
    student_obj = User.objects.get(id=pk)
    return render(request,'student.html',{'student':student_obj})

#metodo que retorna un objeto del tipo UserForm a la vista de form.html
def user_form(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
           user = form.save()
           if user.rol == 'student':
            return redirect('students')
           else:
            return redirect('teachers')   
    context = {'form':form}
    return render(request, 'form.html',context)

