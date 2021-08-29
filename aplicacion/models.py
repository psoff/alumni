from django.db import models
from django.contrib.auth.models import User
class Graduado(models.Model):
    Tesis = 'Tesis'
    Examen = 'Examen complexivo'
    titulacion_opciones = [
        (Tesis, 'Tesis'),
        (Examen, 'Examen complexivo'),
    ]

    Mestizo = 'Mestizo'
    Afroecuatoriano = 'Afroecuatoriano'
    Indígena = 'Indígena'
    Blanco = 'Blanco'
    Montubio = 'Montubio'
    Amazonico = 'Amazonico'
    etnias = [
        (Mestizo, 'Mestizo'),
        (Afroecuatoriano, 'Afroecuatoriano'),
        (Indígena, 'Indígena'),
        (Blanco, 'Blanco'),
        (Montubio, 'Montubio'),
        (Amazonico, 'Amazonico'),
    ]
    Femenino = 'Femenino'
    Masculino ='Masculino'
    generos = [
        (Femenino, 'Femenino'),
        (Masculino, 'Masculino'),
    ]
    Soltero = 'Soltero/a'
    Unión = 'Unión de Hechos'
    Casado ='Casado/a'
    Divorciado = 'Divorciado/a'
    Viudo = 'Viudo/a'
    estadocivil = [
        (Soltero , 'Soltero/a'),
        (Unión , 'Unión de Hechos'),
       (Divorciado , 'Divorciado/a'),
             (Casado ,'Casado/a'),
    (Viudo , 'Viudo/a'),
    ]
    Agroindustrias = 'Agroindustrias'
    Contabilidad = 'Contabilidad'
    DesarrolloInfantil = 'Desarrollo Infantil'
    ProcesamientoAlimentos = 'Procesamiento de Alimentos'
    DesarrolloSoftware = 'Desarrollo de Software'
    Mecanica = 'Mecánica Automotriz'
    Electricidad = 'Electricidad'
    Seguridad = 'Seguridad Ciudadana y Orden Público'
    Taps = 'Atención Primaria de Salud'
    carreras = [
        (Agroindustrias, 'Agroindustrias'),
        (Contabilidad, 'Contabilidad'),
        (DesarrolloInfantil, 'Desarrollo Infantil'),
        (ProcesamientoAlimentos, 'Procesamiento de Alimentos'),
        (DesarrolloSoftware, 'Desarrollo de Software'),
        (Mecanica, 'Mecánica Automotriz'),
        (Electricidad, 'Electricidad'),
        (Seguridad, 'Seguridad Ciudadana y Orden Público'),
        (Taps, 'Atención Primaria de Salud'),
    ]
    Publica = 'Pública'
    Privada = 'Privada'
    Propia = 'Propia'
    tipoempresa = [
        (Publica, 'Pública'),
        (Privada, 'Privada'),
        (Propia, 'Propia'),
    ]
    Completo = 'Tiempo Completo'
    Medio = 'Medio Tiempo'
    Parcial = 'Tiempo Parcial'
    jornada = [
        (Completo, 'Tiempo Completo'),
        (Medio, 'Medio Tiempo'),
        (Parcial, 'Tiempo Parcial'),
    ]
    Ninguno = 'Ninguno'
    Academico = 'Académicos'
    Cultural = 'Culturales'
    Deportivo = 'Deportivos'
    Social = 'Sociales'
    tencuentros = [
        (Ninguno, 'Ninguno'),
        (Academico, 'Académicos'),
        (Cultural, 'Culturales'),
        (Deportivo, 'Deportivos'),
        (Social, 'Sociales'),
    ]
    Urbana = 'Urbana'
    Rural = 'Rural'
    zona = [
        (Urbana, 'Urbana'),
        (Rural, 'Rural')

    ]
    Si = 'Si'
    No = 'No'
    trabaja = [
        (Si, 'Si'),
        (No, 'No')

    ]
    Ninguno = 'Ninguno'
    opc1 = '1-3'
    opc2 = '4-6' 
    opc3 = '7-9'
    opc4 = '10 o más'
    cursos= [
        (Ninguno, 'Ninguno'),
        (opc1,  '1-3'),
        (opc2, '4-6' ),
        (opc3, '7-9' ),
        (opc4, '10 o más' ),

    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='graduado')
    cedula = models.CharField('Cedula', max_length=15)
    imagen = models.ImageField(upload_to = "perfil", null = True, blank = True, default='default.png')
    nombre = models.CharField('Nombre',max_length=250, null = False  )
    apellido = models.CharField('Apellido',max_length=250, null = False)
    direccion = models.CharField('Dirección',max_length=350, blank=True,null = True )
    celular = models.CharField('Celular',max_length=15, null = True , blank = True)
    correo = models.EmailField('Correo', max_length=254,null = False)
    f_nacimiento = models.DateField('Fecha Nacimiento', null = True, blank = True)
    nacionalidad = models.CharField('Nacionalidad',max_length=30,null = True, blank = True)
    etnia = models.CharField('Etnia',choices=etnias,max_length = 50, null = True, blank = True)
    genero = models.CharField('Género', choices=generos ,max_length = 50, null = True, blank = True)
    estado_civil = models.CharField('Estado Civil',choices=estadocivil,max_length = 50,null = True, blank = True)
    discapacidad = models.CharField('Discapacidad',max_length=70,null = True, blank = True)
    carrera = models.CharField('Carrera',choices = carreras,max_length = 50,null = True, blank = True) 
    f_ingreso = models.DateField('Fecha de ingreso a la carrera',null = True, blank = True)
    f_salida = models.DateField('Fecha de graduación',null = True, blank = True)
    n_corte = models.CharField(max_length = 10, null = True, blank = True)
    titulacion = models.CharField(max_length=20,choices=titulacion_opciones,null = True, blank = True)
    trabaja = models.CharField(max_length=10,choices=trabaja,null = True, blank = True)
    empresa = models.CharField( max_length=250,null = True, blank = True)
    tipo_empresa = models.CharField(choices = tipoempresa, max_length = 50,null = True, blank = True) 
    jornada = models.CharField(choices = jornada, max_length = 50,null = True, blank = True) 
    zona = models.CharField(choices = zona, max_length = 50,null = True, blank = True) 
    cargo = models.CharField(max_length = 350,null = True, blank = True) 
    direccion_empresa = models.CharField( max_length = 350,null = True, blank = True) 
    telefono_empresa = models.CharField( max_length = 50,null = True, blank = True) 
    relacion = models.BooleanField(default=True)
    n_cursos = models.CharField(max_length = 20,choices=cursos, null = True, blank = True)
    sugerencia = models.CharField(max_length = 1000, null = True, blank = True)
    tipo_encuentros = models.CharField( choices = tencuentros,max_length = 50,null = True, blank = True) 

    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['cedula','nombre','apellido']

    class Meta:
        verbose_name = 'Graduado'
        
    def __str__(self):
        return f'{self.nombre},{self.apellido}'

    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self,app_lebel):
        return True   

    @property
    def is_staff(self):
        return self.usuario_graduado

class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='administrador', unique = True)
    cedula = models.CharField('Cedula',max_length=15)
    nombre = models.CharField('Nombre',max_length=250)
    apellido = models.CharField('Apellido', max_length=250)
    correo = models.EmailField('Correo', max_length=254)
    imagen = models.ImageField(upload_to = "perfil", null = True, blank = True)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=True)
    REQUIRED_FIELDS = ['cedula','nombre','apellido', 'correo']
    def __str__(self):
        return f'{self.nombre},{self.apellido}'

    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self,app_lebel):
        return True   

    @property
    def is_staff(self):
        return self.usuario_administrador  

    

class Capacitacion (models.Model):
    portada = models.ImageField(upload_to = "capacitacion", null = True, blank= True )
    titulo = models.CharField(max_length=250)
    fecha = models.CharField(max_length=500)
    hora = models.CharField(max_length=500)
    enlace = models.URLField()  
    inversión  = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.titulo}'


class Empleo (models.Model):
    portada = models.ImageField(upload_to = "empleo",default='default.jpg',null = True,blank = True)
    puesto = models.CharField( max_length=100) 
    objetivos = models.CharField( max_length=350)
    experiecia = models.CharField( max_length=350) 
    habilidades = models.CharField( max_length=350)  
    contactos = models.CharField( max_length=850)
    def __str__(self):
        return f'{self.puesto}'

class Emprendimiento (models.Model):   
    portada = models.ImageField(upload_to = "emprendimiento", null = True)
    titulo = models.CharField(max_length=100) 
    descripcion = models.CharField(max_length=1000) 
    propietario = models.CharField(max_length=100) 
    contacto = models.CharField(max_length=100) 
    def __str__(self):
        return f'{self.titulo}' 


