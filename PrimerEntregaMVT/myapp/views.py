from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.forms import RegisterFormulario, RegisterPersona, UserRegisterForm, UserEditForm
from myapp.models import Register, Persona, IntegrantesEmpresa
from django.template import loader

# Login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
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

def persona_formulario(request):
    if request.method == "POST":
        formulario = RegisterPersona(request.POST)
        # Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            # Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data
            persona = Persona(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], 
            profesion=data["profesion"])

            persona.save()

    formulario = RegisterPersona()
    return render(request, "myapp/persona_formulario.html", {"formulario": formulario})

def listadoTrabajadores(request):

    # Se obtienen los datos de la tabla Familiares
    listaIntegrantesEmpresa = Persona.objects.all()

    
    # Se genera un diccionario con la lista
    datos = {
        
        "listaIntegrantesEmpresa": listaIntegrantesEmpresa,

    }

    # Se obtiene el template html
    plantilla = loader.get_template(r"C:\Users\agustin\OneDrive\Escritorio\Curso de python\Myproyect\PrimerEntregaMVT\myapp\templates\myapp\Integrantes_empresa.html")
    
    # Se renderiza datos en la plantilla y se almacena en la variable documento
    documento =  plantilla.render(datos)
    
    # Retorna la variable documento
    return HttpResponse(documento)

def buscar_personas(request):
    return render(request, "myapp/busqueda_personas.html")

def resultado_busqueda_personas(request):
    nombre_persona = request.GET["nombre_persona"]

    personas = Persona.objects.filter(nombre__icontains=nombre_persona)
    return render(request, "myapp/resultado_busquedas_personas.html", {"personas": personas})

def iniciar_sesion(request):

    errors = ""

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["username"], password=data["password"])
            
            if user is not None:
                login(request, user)
                return redirect("web-inicio")
            else:
                return render(request, "myapp/login.html", {"form": formulario, "errors": "Credenciales invalidas"})
        else:
            return render(request, "myapp/login.html", {"form": formulario, "errors": formulario.errors})
    formulario = AuthenticationForm()
    return render(request, "myapp/login.html", {"form": formulario, "errors": errors})

def registrar_usuario(request):

    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            
            formulario.save()
            return redirect("web-inicio")
        else:
            return render(request, "myapp/register.html", { "form": formulario, "errors": formulario.errors})

    formulario  = UserRegisterForm()
    return render(request, "myapp/register.html", { "form": formulario})