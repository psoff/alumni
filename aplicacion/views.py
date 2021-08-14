from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.views.generic import ListView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView



def index(request):

    return render(request,'index.html' )

def informacion(request):

    return render(request,'informacion.html' )  

def base(request):

    return render(request,'base.html' ) 

def emprendimientos(request):

    return render(request,'emprendimientos.html' )     

def servicio(request):

    return render(request,'servicio.html' )         

def ingresar(request):

	return render(request, 'ingresar.html', ) 

@login_required(login_url='ingresar/')
def registro(request):
        if not request.user.is_staff:
            return HttpResponse("No tienes acceso a esta parte.")
        return render(request, 'registro.html') 


def datosform(request):
    if request.method == 'POST':
        form= DatosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Datos guardados con exito')
            form = DatosForm
    else:
        form = DatosForm
    context = {'form': form}            
    return render(request, 'datosform.html', context )   

def paginadmin(request):

	return render(request, 'admin_2.0.html', ) 

def estadistica(request):
    objeto = Graduado.objects.all()
    contexto = {'objeto':objeto}
    return render(request, 'estadistica.html',contexto)   

def baseadmin(request):

	return render(request, 'baseadmin.html', )   

def indexadmin(request):
    objeto = Graduado.objects.all()
    contexto = {'objeto':objeto}
    return render(request, 'index_admin.html',contexto)  

def usuarioform(request):
    if request.method == 'POST':
        form= UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Usuario {username} creado')
            return redirect (indexadmin)
    else:
        form = UserForm
    context = {'form': form}            
    return render(request, 'usuarioform.html', context )   

def graduadoform(request):
    data = { 'form': GraduadoForm()}

    if request.method == 'POST':
        form = GraduadoForm(request.POST)
        if form.is_valid():
            form.save()
            nombre = form.cleaned_data['nombre']
            messages.success(request,f'Usuario {nombre} creado')
        return redirect ('indexadmin')  
    else:
        form = GraduadoForm()      
    return render(request, 'graduadoform.html', {'form':form})
    
def administradorform(request):
    data = { 'form': administradorForm}

    if request.method == 'POST':
        form = administradorForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Usuario {username} creado')
        return redirect ('aplicacion:indexadmin')  
    else:
        form = GraduadoForm()      
    return render(request, 'administradorform.html', {'form':form})    

def capacitacionform(request):
    data = { 'form': CapacitacionForm()}

    if request.method == 'POST':
        form= CapacitacionForm(request.POST)
        if form.is_valid():
            form.save()
            titulo = form.cleaned_data['titulo']
            messages.success(request,f'Capaitación {titulo} creada')            
        return redirect ('aplicacion:capacitacionform')  
    else:
        form = CapacitacionForm()      
    return render(request, 'capacitacionform.html', {'form':form})   

def empleoform(request):
    data = { 'form': EmpleoForm()}

    if request.method == 'POST':
        form = EmpleoForm(request.POST)
        if form.is_valid():
            form.save()
            puesto = form.cleaned_data['puesto']
            messages.success(request,f'Empleo {puesto} creado')            
        return redirect ('aplicacion:empleoform')  
    else:
        form = EmpleoForm()      
    return render(request, 'empleoform.html', {'form':form})   

def emprendimientoform(request):
    data = { 'form': EmprendimientoForm()}

    if request.method == 'POST':
        form = EmprendimientoForm(request.POST)
        if form.is_valid():
            form.save()
            titulo = form.cleaned_data['titulo']
            messages.success(request,f'Emprendimiento {titulo} creado')            
        return redirect ('aplicacion:emprendimientoform')  
    else:
        form = EmprendimientoForm()      
    return render(request, 'emprendimientoform.html', {'form':form})   

def graduadoeditar(request,id):
	object= Graduado.objects.get(id=id)
	if request.method == 'GET':
		form = GraduadoForm(instance=object)	
	else:
		form = GraduadoForm(request.POST,instance=object)
		if form.is_valid():
			form.save()
		return redirect('estadistica')
	return render(request,'graduadoform.html', {'form':form})

def graduadoeliminar(request,id):
	object= Graduado.objects.get(id=id)
	if request.method == 'POST':
		object.delete()
		return redirect('estadistica')
	return render(request,'graduadoeliminar.html', {'object':object})

def graficopastel(request, genero):
    object = Graduado.objects.get(genero=genero).count()

    return render(request,'estadistica.html', {'object':object})
      



    
    
