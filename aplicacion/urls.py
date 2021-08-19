from django.urls import path, include
from .views import *
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import LogoutView, LoginView
from django.conf.urls.static import static

urlpatterns =[
    path('accounts/', include('django.contrib.auth.urls')),
    path('index/',index, name ='index'),
    path('informacion/',informacion, name ='informacion'),
    path('ingresar',LoginView.as_view(template_name='ingresar.html'), name ='ingresar'),
    path('base',base, name ='base'),
    path('logout',LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name ='logout'),
    path('datosform',datosform, name ='datosform'),
    path('estadistica',estadistica, name ='estadistica'),
    path('baseadmin',baseadmin, name ='baseadmin'),
    path('indexadmin',indexadmin, name ='indexadmin'),
    path('graduadoform',graduadoform, name ='graduadoform'),
    path('administradorform',administradorform, name ='administradorform'),
    path('emprendimientos',emprendimientos, name ='emprendimientos'),
    path('empleos',empleos, name ='empleos'),
    path('capacitaciones',capacitaciones, name = 'capacitaciones'),
    path('capacitacionform',capacitacionform, name = 'capacitacionform'),
    path('empleoform',empleoform, name = 'empleoform'),
    path('emprendimientoform',emprendimientoform, name = 'emprendimientoform'),
    path('usuarioform',usuarioform, name = 'usuarioform'),
    path('graduadoeditar/<id>/' ,graduadoeditar, name='graduadoeditar'),
    path('graduadoeliminar/<id>/' ,graduadoeliminar, name='graduadoeliminar'),
    path('admineditar/<id>/' ,admineditar, name='admineditar'),
    path('admineliminar/<id>/' ,admineliminar, name='admineliminar'),
]