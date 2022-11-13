from django.urls import path
from myapp.views import *

urlpatterns = [
    path("", inicio, name= "web-inicio"),
    path("about", about, name= "web-about"),
    path("crear/", register , name= "count-register"),
]