# Generated by Django 3.2.3 on 2021-08-28 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0011_remove_graduado_cursos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graduado',
            name='encuentros',
        ),
        migrations.AlterField(
            model_name='graduado',
            name='carrera',
            field=models.CharField(blank=True, choices=[('Agroindustrias', 'Agroindustrias'), ('Contabilidad', 'Contabilidad'), ('Desarrollo Infantil', 'Desarrollo Infantil'), ('Procesamiento de Alimentos', 'Procesamiento de Alimentos'), ('Desarrollo de Software', 'Desarrollo de Software'), ('Mecánica Automotriz', 'Mecánica Automotriz'), ('Electricidad', 'Electricidad'), ('Seguridad Ciudadana y Orden Público', 'Seguridad Ciudadana y Orden Público'), ('Atención Primaria de Salud', 'Atención Primaria de Salud')], max_length=50, null=True, verbose_name='Carrera'),
        ),
        migrations.AlterField(
            model_name='graduado',
            name='direccion_empresa',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='graduado',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('Soltero/a', 'Soltero/a'), ('Unión de Hechos', 'Unión de Hechos'), ('Divorciado/a', 'Divorciado/a'), ('Casado/a', 'Casado/a'), ('Viudo/a', 'Viudo/a')], max_length=50, null=True, verbose_name='Estado Civil'),
        ),
        migrations.AlterField(
            model_name='graduado',
            name='etnia',
            field=models.CharField(blank=True, choices=[('Mestizo', 'Mestizo'), ('Afroecuatoriano', 'Afroecuatoriano'), ('Indígena', 'Indígena'), ('Blanco', 'Blanco'), ('Montubio', 'Montubio'), ('Amazonico', 'Amazonico')], max_length=50, null=True, verbose_name='Etnia'),
        ),
        migrations.AlterField(
            model_name='graduado',
            name='jornada',
            field=models.CharField(blank=True, choices=[('Tiempo Completo', 'Tiempo Completo'), ('Medio Tiempo', 'Medio Tiempo'), ('Tiempo Parcial', 'Tiempo Parcial')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='graduado',
            name='telefono_empresa',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='graduado',
            name='tipo_empresa',
            field=models.CharField(blank=True, choices=[('Pública', 'Pública'), ('Privada', 'Privada'), ('Propia', 'Propia')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='graduado',
            name='tipo_encuentros',
            field=models.CharField(blank=True, choices=[('Ninguno', 'Ninguno'), ('Académicos', 'Académicos'), ('Culturales', 'Culturales'), ('Deportivos', 'Deportivos'), ('Sociales', 'Sociales')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='graduado',
            name='titulacion',
            field=models.CharField(blank=True, choices=[('Tesis', 'Tesis'), ('Examen complexivo', 'Examen complexivo')], max_length=20, null=True),
        ),
    ]