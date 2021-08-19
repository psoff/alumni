from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.views.generic import ListView
from django.contrib import messages
from django.http import HttpResponseRedirect


def index(request):

    return render(request,'index.html' )

def informacion(request):

    return render(request,'informacion.html' )  

def base(request):

    return render(request,'base.html' ) 
 

def emprendimientos(request):
    objeto= Emprendimiento.objects.all()
    contexto = {'objeto':objeto}

    return render(request,'emprendimientos.html' , contexto)     

@login_required(login_url='ingresar/')
def empleos(request):
    objeto= Empleo.objects.all()
    contexto = {'objeto':objeto}

    return render(request,'empleos.html', contexto )  

@login_required(login_url='ingresar/')
def capacitaciones(request):
    objeto= Capacitacion.objects.all()
    contexto = {'objeto':objeto}

    return render(request,'capacitaciones.html', contexto )  


@login_required(login_url='ingresar/')
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



def estadistica(request):
    objeto = Graduado.objects.all()
    admin = Administrador.objects.all()
    masculino = objeto.filter(genero='Masculino').count() / objeto.count() * 100
    femenino = objeto.filter(genero='Femenino').count() / objeto.count() * 100
    agroindustrias = objeto.filter(carrera='Agroindustrias').count() / objeto.count() * 100
    contabilidad = objeto.filter(carrera='Contabilidad').count() / objeto.count() * 100
    desarrolloinfantil = objeto.filter(carrera='Desarrollo Infantil').count() / objeto.count() * 100
    procesamientoalimentos = objeto.filter(carrera='Procesamiento de Alimentos').count() / objeto.count() * 100
    desarrollosoftware = objeto.filter(carrera='Desarrollo de Software').count() / objeto.count() * 100
    mecanica = objeto.filter(carrera='Mecánica Automotriz').count() / objeto.count() * 100
    electricidad = objeto.filter(carrera='Electricidad').count() / objeto.count() * 100
    seguridad = objeto.filter(carrera= 'Seguridad Ciudadana y Orden Público').count() / objeto.count() * 100
    mestizo= objeto.filter(etnia='Mestizo').count() / objeto.count() * 100
    afroecuatoriano= objeto.filter(etnia='Afroecuatoriano').count() / objeto.count() * 100
    indigena= objeto.filter(etnia='Indígena').count() / objeto.count() * 100
    blanco= objeto.filter(etnia='Blanco').count() / objeto.count() * 100
    montubio= objeto.filter(etnia='Montubio').count() / objeto.count() * 100
    amazonico= objeto.filter(etnia='Amazonico').count() / objeto.count() * 100
    tesis= objeto.filter(titulacion='Tesis').count() / objeto.count() * 100
    examen= objeto.filter(titulacion='Examen Complexivo').count() / objeto.count() * 100

 
    contexto = {'objeto':objeto,
        
        'masculino': round(masculino),
        'femenino': round(femenino),
        'agroindustrias': round(agroindustrias),
        'contabilidad': round(contabilidad),
        'desarrolloinfantil': round(desarrolloinfantil),
        'procesamientoalimentos': round(procesamientoalimentos),
        'desarrollosoftware': round(desarrollosoftware),
        'mecanica': round(mecanica),
        'electricidad': round(electricidad),
        'seguridad': round(seguridad),
        'mestizo': round(mestizo),
        'afroamericano': round(afroecuatoriano),
        'indigena': round(indigena),
        'blanco': round(blanco),
        'montubio': round(montubio),
        'amazonico': round(amazonico),
        'tesis': round(tesis),
        'examen': round(examen),

        }

   
    return render(request, 'estadistica.html',contexto)   

def baseadmin(request):

	return render(request, 'baseadmin.html', )   

def indexadmin(request):
    admin= Administrador.objects.all()
    contexto = {'admin':admin}
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
    data = { 'form': AdministradorForm()}

    if request.method == 'POST':
        form = AdministradorForm(request.POST)
        if form.is_valid():
            form.save()
            nombre= form.cleaned_data['nombre']
            messages.success(request,f'Usuario {nombre} creado')
        return redirect ('indexadmin')  
    else:
        form = AdministradorForm()      
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

def admineditar(request,id):
	admin= Administrador.objects.get(id=id)
	if request.method == 'GET':
		form = administradorForm(instance=admin)	
	else:
		form = administradorForm(request.POST,instance=admin)
		if form.is_valid():
			form.save()
		return redirect('estadistica')
	return render(request,'administradorform.html', {'form':form})

def admineliminar(request,id):
	admin= Administrador.objects.get(id=id)
	if request.method == 'POST':
		admin.delete()
		return redirect('estadistica')
	return render(request,'admineliminar.html', {'admin':admin})    




    
    
