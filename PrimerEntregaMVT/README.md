# MY web 

# como ingresar a las rutas?
Agregamos "/myweb/" y luego las rutas a las que se quieren acceder

 urlpatterns = [
    path("", inicio, name= "web-inicio"),
    path("about", about, name= "web-about"),
    path("register/", register , name= "web-register"),
    path("crear/trabajador/", persona_formulario , name= "web-register-trabajador"),
    path("listado/trabajadores/", listadoTrabajadores, name= "web-listado-trabajadores")
]