from django.urls import path
from myapp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name= "web-inicio"),
    path("about", about, name= "web-about"),
    
    
    path("crear/trabajador/", persona_formulario , name= "web-register-trabajador"),
    path("listado/trabajadores/", listadoTrabajadores, name= "web-listado-trabajadores"),
    path("buscar/personas/", buscar_personas, name= "myweb-buscar-personas"),
    path("buscar/personas/resultados/", resultado_busqueda_personas, name= "myweb-buscar-personas-resultados"),

    path("login/", iniciar_sesion, name="auth-login"),
    path("register/", registrar_usuario, name="auth-register"),
    path("logout/", LogoutView.as_view(), name="auth-logout"),
    path("perfil/editar/", editar_perfil, name="auth-editar-perfil"),
    path("perfil/avatar/", agregar_avatar, name="auth-avatar")
]