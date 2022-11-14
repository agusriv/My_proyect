# MY web 

# Como ingresar a las rutas?
("myweb/") es la ruta prinicipal para ingresar a las demas ponemos "myweb/" y las rutas que vemos a acontinuación son las disponibles

```python
urlpatterns = [
    path("", inicio, name= "web-inicio"),
    path("about", about, name= "web-about"),
    path("register/", register , name= "web-register"),
    path("crear/trabajador/", persona_formulario , name= "web-register-trabajador"),
    path("listado/trabajadores/", listadoTrabajadores, name= "web-listado-trabajadores")
]
```
# Funciones

En la web se pueden registrar personas, crear un trabajador y luego listarlos 
