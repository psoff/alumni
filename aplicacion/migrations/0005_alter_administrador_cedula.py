# Generated by Django 3.2.3 on 2021-08-21 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_alter_graduado_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='cedula',
            field=models.CharField(max_length=15, verbose_name='Cedula'),
        ),
    ]
