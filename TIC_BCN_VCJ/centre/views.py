from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context , loader
from django.shortcuts import render , redirect
from .forms import UserForm #importamos la clase UserForm 
from .models import User
# Create your views here.

#endPoint que retorna una vista de bienvenida
def welcome(request):

    return render(request,'index_centre.html')

#endPoint que va hacia la vista de teachers on el objeto con la informacion recuperada de la base de datos
#filtrada por rol
def teacher(request):
  
    teachersData = User.objects.filter(rol='teacher')
    return render(request,'index_teachers.html',{'data':teachersData})

#endPoint que va hacia la vista de students con el objeto con la informacion recuperada de la base de datos
#filtrada por rol
def student(request):
    studentsData = User.objects.filter(rol='student')
    return render(request,'index_students.html',{'data':studentsData})
#recibe por parametro la id y realiza el filtro en la base de datos y envia el objeto que coincide
def teacherInfo(request, pk):
    teacher_obj = User.objects.get(id=pk)
    return render(request,'teacher.html',{'teacher':teacher_obj})

#recibe por parametro la id y realiza el filtro en la base de datos y envia el objeto que coincide
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

# metodo que actualiza la instancia user
# recupera la instancia por la id retorna al form.html para editar 
# verificamos que el metodo sea POST, validamos y guardamos los datos
# segun el rol retorna a una vista u otra
def update_user(request,pk):
   user_obj = User.objects.get(id=pk)
   form = UserForm(instance=user_obj)
   is_update = True
   rol_user = user_obj.rol
   if request.method == 'POST':
        form = UserForm(request.POST, instance=user_obj)
        if form.is_valid():
            user = form.save()
            if user.rol == 'student':            
                return redirect('students')
            else:
                return redirect('teachers') 
   context = {'form':form,
              'is_update': is_update,
              'rol': rol_user} 
   return render(request, 'form.html',context)

# metodo que elimina la instancia user
# recupera la instancia por la id retorna al delete_form.html para reconfirmar la accion 
# retorna y verificamos que el metodo sea POST, eliminamos los datos
# y retorna a la pagina principal
def delete_user(request,pk):
    user_obj = User.objects.get(id=pk)
    if request.method == 'POST':
       user_obj.delete()
       return redirect('centre')
    context = {'user':user_obj} 
    return render(request, 'delete_form.html',context)
          
    