from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from .models import *
from .forms import *
from django.views.generic import ListView, UpdateView
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.views import LoginView  
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt



def index(request):

    return render(request,'index.html' )

def informacion(request):

    return render(request,'informacion.html' )  

def base(request):

    return render(request,'base.html' ) 
 
def emprendimientos(request):
    emprendimientos = Emprendimiento.objects.all()
    contexto = {'emprendimientos':emprendimientos}

    return render(request,'emprendimientos.html' , contexto)     

class LoginFormView(LoginView):
    template_name = 'ingresar.html'

    def validarUsuario(request):
        if request.user.is_authenticated():
            if request.user.is_staff:
                return redirect('indexadmin')
            else:
                return redirect('index')
        return redirect('ingresar')
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context


def VaUsuario(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return redirect('indexadmin')
        else:
            return redirect('index')
    return redirect('ingresar')

@login_required(login_url='ingresar/')
def empleos(request):
    empleos= Empleo.objects.all()
    contexto = {'empleos':empleos}

    return render(request,'empleos.html', contexto )  

@login_required(login_url='ingresar/')
def capacitaciones(request):
    capacitaciones= Capacitacion.objects.all()
    contexto = {'capacitaciones':capacitaciones}

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
    Ninguno = objeto.filter(n_cursos = 'Ninguno').count() / objeto.count() * 100
    opc1 = objeto.filter(n_cursos = '1-3').count() / objeto.count() * 100
    opc2 = objeto.filter(n_cursos = '4-6').count() / objeto.count() * 100
    opc3 = objeto.filter(n_cursos = '7-9').count() / objeto.count() * 100
    opc4 = objeto.filter(n_cursos = '10 o más').count() / objeto.count() * 100
    si = objeto.filter(n_cursos = 'Si').count() / objeto.count() * 100
    no = objeto.filter(n_cursos = 'No').count() / objeto.count() * 100
 
    contexto = {'objeto':objeto,
        'admin':admin,
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
        'ninguno': round(Ninguno),
        'opc1':round(opc1),
        'opc2':round(opc2),
        'opc3':round(opc3),
        'opc4':round(opc4),
        'si':round(si),
        'no':round(no),

        }

   
    return render(request, 'estadistica.html',contexto)   

def baseadmin(request):

	return render(request, 'baseadmin.html', )   

def indexadmin(request):
    admin= Administrador.objects.all()
    capacitacion = Capacitacion.objects.all()
    empleo = Empleo.objects.all()
    emprendimiento = Emprendimiento.objects.all()
    contexto = {'admin':admin,
                'capacitacion': capacitacion,
                'empleo': empleo,
                'emprendimiento': emprendimiento}
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
        form = GraduadoForm(request.POST,request.FILES)
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
        form = AdministradorForm(request.POST,request.FILES)
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
        form= CapacitacionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            titulo = form.cleaned_data['titulo']
            messages.success(request,f'Capaitación {titulo} creada')            
        return redirect ('index')  
    else:
        form = CapacitacionForm()      
    return render(request, 'capacitacionform.html', {'form':form})   

def empleoform(request):
    if request.method == 'POST':
        form= EmpleoForm(request.POST,  request.FILES)
        if form.is_valid():
            form.save()
            puesto = form.cleaned_data['puesto']
            messages.success(request,f'Empleo {puesto} creado')
            return redirect ('index')
    else:
        form = EmpleoForm()
    context = {'form': form}            
    return render(request, 'empleoform.html', context )  

 

def emprendimientoform(request):
    data = { 'form': EmprendimientoForm()}

    if request.method == 'POST':
        form = EmprendimientoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            titulo = form.cleaned_data['titulo']
            messages.success(request,f'Emprendimiento {titulo} creado')            
        return redirect ('emprendimientoform')  
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
		form = AdministradorForm(instance=admin)	
	else:
		form = AdministradorForm(request.POST,instance=admin)
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

def capacitacioneditar(request,id):
	capacitacion= Capacitacion.objects.get(id=id)
	if request.method == 'GET':
		form = CapacitacionForm(instance=capacitacion)	
	else:
		form = CapacitacionForm(request.POST,instance=capacitacion)
		if form.is_valid():
			form.save()
		return redirect('indexadmin')
	return render(request,'capacitacionform.html', {'form':form})
	
def capacitacioneliminar(request,id):
	capacitacion= Capacitacion.objects.get(id=id)
	if request.method == 'POST':
		capacitacion.delete()
		return redirect('estadistica')
	return render(request,'capacitacioneliminar.html', {'capacitacion':capacitacion})

def empleoditar(request,id):
	empleo= Empleo.objects.get(id=id)
	if request.method == 'GET':
		form = EmpleoForm(instance=empleo)	
	else:
		form = EmpleoForm(request.POST,instance=empleo)
		if form.is_valid():
			form.save()
		return redirect('indexadmin')
	return render(request,'empleoform.html', {'form':form})
	
def empleoeliminar(request,id):
	empleo= Empleo.objects.get(id=id)
	if request.method == 'POST':
		empleo.delete()
		return redirect('indexadmin')
	return render(request,'empleoeliminar.html', {'empleo':empleo})

def emprendimientoeditar(request,id):
	emprendimiento= Emprendimiento.objects.get(id=id)
	if request.method == 'GET':
		form = EmprendimientoForm(instance=emprendimiento)	
	else:
		form = EmprendimientoForm(request.POST,instance=emprendimiento)
		if form.is_valid():
			form.save()
		return redirect('indexadmin')
	return render(request,'emprendimientoform.html', {'form':form})
	

def emprendimientoeliminar(request,id):
	emprendimiento=Emprendimiento.objects.get(id=id)
	if request.method == 'POST':
		emprendimiento.delete()
		return redirect('indexadmin')
	return render(request,'emprendimientoeliminar.html', {'emprendimiento':emprendimiento})


def registro(request):
    if request.method == 'POST':
       form = UserForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data['username']
           messages.success(request,f'Usuario {username} creado')
           return redirect('indexadmin')
    else:
        form = UserForm()
    context ={ 'form' : form}    
    return render(request,'usuarioform.html', context) 

@login_required
def actperfil(request):
    user = request.user.id
    perfil = Graduado.objects.get(user_id=user)
    

    if request.method == 'POST':
        user = request.user.id
        perfil = Graduado.objects.get(user_id=user)
        form = DatosForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DatosForm(instance=perfil)

    contexto= {'form':form}
    return render(request, 'datosform.html',contexto)


