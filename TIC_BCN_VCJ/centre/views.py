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