from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import RegisterFormulario
from myapp.models import Register 

# Create your views here.

def inicio(request):
    return render(request, "myapp/inicio.html")

def about(request):
    return render(request, "myapp/about.html")

def register(request):
    if request.method == "POST":
        formulario = RegisterFormulario(request.POST)
        # Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            # Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data
            register = Register(nombre=data["nombre"], apellido=data["apellido"], email=data["email"])

            register.save()

    formulario = RegisterFormulario()
    return render(request, "myapp/register_formulario.html", {"formulario": formulario})