# My web 

## Como ingresar a las rutas?
("myweb/") es la ruta prinicipal para ingresar a las demas ponemos "myweb/" y las rutas que vemos a acontinuación son las disponibles

## Rutas
```python
urlpatterns = [
    path("", inicio, name= "web-inicio"),
    path("about", about, name= "web-about"),
    path("register/", register , name= "web-register"),
    path("crear/trabajador/", persona_formulario , name= "web-register-trabajador"),
    path("listado/trabajadores/", listadoTrabajadores, name= "web-listado-trabajadores"),
    path("buscar/personas/", buscar_personas, name= "myweb-buscar-personas"),
    path("buscar/personas/resultados/", resultado_busqueda_personas, name= "myweb-buscar-personas-resultados")
]

```
## Funciones

En la web se pueden registrar personas, crear un trabajador, listar los trabajadores y también se pueden buscar las personas registradas
