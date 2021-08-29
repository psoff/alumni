# Generated by Django 3.2.3 on 2021-08-28 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0006_alter_graduado_cedula'),
    ]

    operations = [
        migrations.AddField(
            model_name='graduado',
            name='cursos',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='graduado',
            name='direccion_empresa',
            field=models.CharField(blank=True, max_length=350, null=True, verbose_name='Dirección de empresa'),
        ),
        migrations.AddField(
            model_name='graduado',
            name='empresa',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='graduado',
            name='encuentros',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='graduado',
            name='jornada',
            field=models.CharField(blank=True, choices=[('Tiempo Completo', 'Tiempo Completo'), ('Medio Tiempo', 'Medio Tiempo'), ('Tiempo Parcial', 'Tiempo Parcial')], default='Tiempo Completo', max_length=50, null=True, verbose_name='Jornada Laboral'),
        ),
        migrations.AddField(
            model_name='graduado',
            name='n_corte',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='graduado',
            name='n_cursos',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='graduado',
            name='razon',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='graduado',
            name='relacion',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='graduado',
            name='sugerencia',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='graduado',
            name='telefono_empresa',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Teléfono de empresa'),
        ),
        migrations.AddField(
            model_name='graduado',
            name='tipo_empresa',
            field=models.CharField(blank=True, choices=[('Pública', 'Pública'), ('Privada', 'Privada'), ('Propia', 'Propia')], default='Privada', max_length=50, null=True, verbose_name='Tipo de empresa'),
        ),
        migrations.AddField(
            model_name='graduado',
            name='tipo_encuentros',
            field=models.CharField(blank=True, choices=[('Académicos', 'Académicos'), ('Culturales', 'Culturales'), ('Deportivos', 'Deportivos'), ('Sociales', 'Sociales')], default='Académicos', max_length=50, null=True, verbose_name='Tipo de Encuentros'),
        ),
        migrations.AddField(
            model_name='graduado',
            name='trabaja',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='graduado',
            name='carrera',
            field=models.CharField(blank=True, choices=[('Agroindustrias', 'Agroindustrias'), ('Contabilidad', 'Contabilidad'), ('Desarrollo Infantil', 'Desarrollo Infantil'), ('Procesamiento de Alimentos', 'Procesamiento de Alimentos'), ('Desarrollo de Software', 'Desarrollo de Software'), ('Mecánica Automotriz', 'Mecánica Automotriz'), ('Electricidad', 'Electricidad'), ('Seguridad Ciudadana y Orden Público', 'Seguridad Ciudadana y Orden Público'), ('Atención Primaria de Salud', 'Atención Primaria de Salud')], default='Agroindustrias', max_length=50, null=True, verbose_name='Carrera'),
        ),
    ]
