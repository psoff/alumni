from django import forms
from django.contrib.auth.forms import UserCreationForm
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
            'user': forms.TextInput(attrs={'class':'form-control'}),
            'cedula': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            
        }

class AdministradorForm(forms.ModelForm):
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
            'user': forms.TextInput(attrs={'class':'form-control'}),
            'cedula': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.TextInput(attrs={'class':'form-control'}),
        }

class CapacitacionForm(forms.ModelForm):
    class Meta:
        model = Capacitacion
        fields = [
            'portada',
            'titulo',
            'fecha',
            'hora',
            'enlace',
            'inversión']
        labels = {
            'portada' : 'Portada',
            'titulo' : 'Titulo',
            'fecha': 'Fecha',
            'hora' : 'Hora',
            'enlace' : 'Enlace',
            'inversión' : 'Inversión'
        }
        widgets = {
            'portada':forms.FileInput(attrs={'class':'form-control mb-3 '}),
            'titulo': forms.TextInput(attrs={'class':'form-control mb-2'}),
            'fecha': forms.TextInput(attrs={'class':'form-control mb-2'}),
            'hora': forms.TextInput(attrs={'class':'form-control mb-2'}),
            'enlace': forms.TextInput(attrs={'class':'form-control mb-2'}),
            'inversión': forms.TextInput(attrs={'class':'form-control mb-2'}),
        }

class EmpleoForm(forms.ModelForm):
    class Meta:
        model = Empleo
        fields = [
            'portada',
            'puesto',
            'objetivos',
            'experiecia',
            'habilidades',
            'contactos']
        labels = {
            'portada': 'Portada',
            'puesto':'Puesto',
            'objetivos': 'Objetivos',
            'experiecia':'Experiencia',
            'habilidades': 'Habilidades',
            'contactos':'Contactos',
        }
        widgets = {
            'portada':forms.FileInput(attrs={'class':'form-control mb-3 '}),
            'puesto': forms.TextInput(attrs={'class':'form-control mb-2 '}),
            'objetivos': forms.TextInput(attrs={'class':'form-control mb-2'}),
            'experiecia': forms.TextInput(attrs={'class':'form-control' }),
            'habilidades': forms.TextInput(attrs={'class':'form-control mb-2 '}),
            'contactos': forms.TextInput(attrs={'class':'form-control '}),
          
        }

class EmprendimientoForm(forms.ModelForm):
    class Meta:
        model = Emprendimiento
        fields = [
            'portada',
            'titulo',
            'descripcion',
            'propietario',
            'contacto']  
        labels = {
            'portada':'Portada',
            'titulo':'Titulo',
            'descripcion':'Descripcion',
            'propietario':'Propietario',
            'contacto':'Contacto',
        }
        widgets = {
            'portada':forms.FileInput(attrs={'class':'form-control mb-3 '}),
            'titulo': forms.TextInput(attrs={'class':'form-control mb-2 '}),
            'descripcion': forms.TextInput(attrs={'class':'form-control mb-2'}),
            'propietario': forms.TextInput(attrs={'class':'form-control mb-2'}),
            'contacto': forms.TextInput(attrs={'class':'form-control mb-2'}),
        }

class UserForm(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    # this Meta class is the way we send information for our form
    class Meta:
        # define the model
        model = User
        # define the fields you need (note that username and password are required)
        fields = [
            'username',
            'password1',
            'password2',
            'is_staff',
        ]
        labels = {
            'username': 'Usuario',
            'password1': 'Contraseña', 
            'password2': 'Confirmar Contraseña', 
            'is_staff': 'Administrador',
        }
        # then, in widgets you can define the input type of the field and give
        # attributes to each one
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control col-sm-8'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control mb-2 col-sm-8'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control mb-2 col-sm-8'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input  col.6'}),
        } 
        help_texts = {k:"" for k in fields}   

class DatosForm(forms.ModelForm):
  
    class Meta:
        model = Graduado
        fields = [
            'cedula',
            'nombre',
            'apellido',
            'imagen',
            'direccion',
            'celular',
            'correo',
            'estado_civil',
            'discapacidad',
            'trabaja',
            'empresa', 
            'tipo_empresa' , 
            'jornada' ,
            'zona',
            'cargo',
            'direccion_empresa' ,
            'telefono_empresa' ,
            'relacion',
            'n_cursos', 
            'sugerencia',
            'tipo_encuentros', 


            ]
        labels = {
            'cedula' : 'Cedula',
            'nombre': 'Nombre',
            'apellido' : 'Apellido',
            'imagen':'Imagen',
            'direccion':'Direccion',
            'celular':'Celular',
            'correo':'Correo',
            'estado_civil': 'Estado civil',
            'discapacidad': 'Discapacidad', 
            'trabaja': 'Se encuentra trabajando actualmente',
            'empresa': 'Nombre de la empresa o institución en la que labora', 
            'tipo_empresa':'Tipo de empresa o institución en la que labora' , 
            'jornada':'Jornada en la que labora' ,
            'zona': 'Zona en la que esta ubicada la empresa o institución en la que labora ',
            'cargo':'Cargo que desempeña en la empresa o institución en la que labora',
            'direccion_empresa': 'Dirección de la empresa o institución en la que trabaja' ,
            'telefono_empresa':'Teléfono de la empresa o institución en la que labora' ,
            'relacion':'La empresa donde trabaja es acorde a su profesión.',
            'n_cursos': 'Cuántos cursos dictados por el ISTL ha tomado', 
            'sugerencia': 'Que cursos le gustaría seguir en el ISTl',
            'tipo_encuentros': 'Tipos de Encuentros', 
        }
        widgets = {
            'cedula': forms.TextInput(attrs={'class':'form-control mb-2  ', 'disabled': 'true'}),
            'nombre': forms.TextInput(attrs={'class':'form-control mb-3', 'disabled': 'true'}),
            'apellido': forms.TextInput(attrs={'class':'form-control ', 'disabled': 'true'}),
            'imagen':forms.FileInput(attrs={'class':'form-control mb-3 '}),
            'direccion': forms.TextInput(attrs={'class':'form-control '}),
            'celular':forms.TextInput(attrs={'class':'form-control'}),
            'correo':forms.TextInput(attrs={'class':'form-control'}),
            'estado_civil': forms.Select(attrs={'class':'form-select'}),
            'discapacidad':forms.TextInput(attrs={'class':'form-control mb-2'}),
            'trabaja': forms.Select(attrs={'class':'form-select mb-2'}),
            'empresa': forms.TextInput(attrs={'class':'form-control'}), 
            'tipo_empresa':  forms.Select(attrs={'class':'form-select mb-2'}),  
            'jornada':  forms.Select(attrs={'class':'form-select mb-2'}) ,
            'zona':  forms.Select(attrs={'class':'form-select mb-2'}) ,
            'cargo' : forms.TextInput(attrs={'class':'form-control'}),
            'direccion_empresa' : forms.TextInput(attrs={'class':'form-control'}),
            'telefono_empresa': forms.TextInput(attrs={'class':'form-control'}), 
            'relacion': forms.CheckboxInput(attrs={'class': 'form-check-label'}), 
            'cursos':  forms.CheckboxInput(attrs={'class': 'form-check-input'}), 
            'n_cursos': forms.Select(attrs={'class':'form-select'}),
            'sugerencia': forms.TextInput(attrs={'class':'form-control'}),
            'encuentros': forms.CheckboxInput(attrs={'class': 'form-check-input'}), 
            'tipo_encuentros': forms.Select(attrs={'class':'form-select mb-2'}),    


        }
