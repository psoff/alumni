from django import forms
from .models import *


class GraduadoForm(forms.ModelForm):
    class Meta:
        model = Graduado
        fields = [
            'user',
            'cedula',
            'nombre',
            'apellido',
            ]
        labels = {
            'user' : 'Usuario',
            'cedula' : 'Cedula',
            'nombre': 'Nombre',
            'apellido' : 'Apellido',
        }
        widgets = {
            'user': forms.Select(attrs={'class':'form-control'}),
            'cedula': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            
        }

class administradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields =['user',
            'cedula',
            'nombre',
            'apellido',
            'correo'] 
        labels = {
            'user' : 'Usuario',
            'cedula' : 'Cedula',
            'nombre': 'Nombre',
            'apellido' : 'Apellido',
            'correo' : 'Correo',
        }
        widgets = {
            'user': forms.Select(attrs={'class':'form-control '}),
            'cedula': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.TextInput(attrs={'class':'form-control'}),
        }

class CapacitacionForm(forms.ModelForm):
    class Meta:
        model = Capacitacion
        fields = ['titulo',
            'fecha',
            'hora',
            'enlace',
            'inversión']
        labels = {
            'titulo' : 'Titulo',
            'fecha': 'Fecha',
            'hora' : 'Hora',
            'enlace' : 'Enlace',
            'inversión' : 'Inversión'
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control mb-2'}),
            'fecha': forms.TextInput(attrs={'class':'form-control mb-2'}),
            'hora': forms.TextInput(attrs={'class':'form-control mb-2'}),
            'enlace': forms.TextInput(attrs={'class':'form-control mb-2'}),
            'inversión': forms.TextInput(attrs={'class':'form-control mb-2'}),
        }

class EmpleoForm(forms.ModelForm):
    class Meta:
        model = Empleo
        fields = ['puesto',
            'objetivos',
            'experiecia',
            'habilidades',
            'contactos']
        labels = {
            'puesto':'Puesto',
            'objetivos': 'Objetivos',
            'experiecia':'Experiencia',
            'habilidades': 'Habilidades',
            'contactos':'Contactos',
        }
        widgets = {
            'puesto': forms.TextInput(attrs={'class':'form-control mb-2 '}),
            'objetivos': forms.TextInput(attrs={'class':'form-control mb-2'}),
            'experiecia': forms.TextInput(attrs={'class':'form-control' }),
            'habilidades': forms.TextInput(attrs={'class':'form-control mb-2 '}),
            'contactos': forms.TextInput(attrs={'class':'form-control '}),
          
        }

class EmprendimientoForm(forms.ModelForm):
    class Meta:
        model = Emprendimiento
        fields = ['titulo',
            'descripcion',
            'propietario',
            'contacto']  
        labels = {
            'titulo':'Titulo',
            'descripcion':'Descripcion',
            'propietario':'Propietario',
            'contacto':'Contacto',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control mb-2 '}),
            'descripcion': forms.TextInput(attrs={'class':'form-control mb-2'}),
            'propietario': forms.TextInput(attrs={'class':'form-control mb-2'}),
            'contacto': forms.TextInput(attrs={'class':'form-control mb-2'}),
        }

class UserForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    # this Meta class is the way we send information for our form
    class Meta:
        # define the model
        model = User
        # define the fields you need (note that username and password are required)
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'is_staff',
        ]
        labels = {
            'username': 'Usuario',
            'password': 'Contraseña',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'is_staff': 'Es administrador',
        }
        # then, in widgets you can define the input type of the field and give
        # attributes to each one
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control col-sm-8'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control mb-2 col-sm-8'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control mb-2 col-sm-8'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mb-2 col-sm-8'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input mb-2 col-sm-1'}),
        } 
        help_texts = {k:"" for k in fields}   

class DatosForm(forms.ModelForm):
    class Meta:
        model = Graduado
        fields = [
            'cedula',
            'imagen',
            'nombre',
            'apellido',
            'direccion',
            'celular',
            'correo',
            'f_nacimiento',
            'nacionalidad',
            'etnia',
            'genero',
            'estado_civil',
            'discapacidad',
            'carrera',
            'f_ingreso',
            'f_salida',
            'titulacion',
            ]
        labels = {
            'user' : 'Usuario',
            'cedula' : 'Cedula',
            'imagen':'Imagen',
            'nombre': 'Nombre',
            'apellido' : 'Apellido',
            'direccion':'Direccion',
            'celular':'Celular',
            'correo':'Correo',
            'f_nacimiento': 'Fecha Nacimiento',
            'nacionalidad': 'Nacionalidad',
            'etnia': 'Etnia',
            'genero': 'Género',
            'estado_civil': 'Estado Civil',
            'discapacidad': 'Discapacidad',
            'carrera':'Carrera',
            'f_ingreso': 'Fecha Ingreso',
            'f_salida':'Fecha Salida',
            'titulacion': 'Titulación',
        }
        widgets = {
            'user': forms.Select(attrs={'class':'form-control '}),
            'cedula': forms.TextInput(attrs={'class':'form-control mb-2 '}),
            'imagen':forms.FileInput(attrs={'class':'form-control mb-3 '}),
            'nombre': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'apellido': forms.TextInput(attrs={'class':'form-control '}),
            'direccion': forms.TextInput(attrs={'class':'form-control '}),
            'celular':forms.TextInput(attrs={'class':'form-control'}),
            'correo':forms.TextInput(attrs={'class':'form-control'}),
            'f_nacimiento': forms.DateInput(format='%d-%m-%Y'),
            'nacionalidad': forms.TextInput(attrs={'class':'form-control'}),
            'etnia': forms.Select(attrs={'class':'form-select'}),
            'genero': forms.Select(attrs={'class':'form-select'}),
            'estado_civil': forms.Select(attrs={'class':'form-select'}),
            'discapacidad':forms.TextInput(attrs={'class':'form-control'}),
            'carrera': forms.Select(attrs={'class':'form-select mb-2'}),
            'f_ingreso': forms.DateInput(format='%d-%m-%Y', attrs={'class':'form-control mb-3'} ),
            'f_salida': forms.DateInput(format='%d-%m-%Y', attrs={'class':'form-control mb-3'}),
            'titulacion': forms.Select(attrs={'class':'form-select mb-3'}),


        }