# Generated by Django 3.2.3 on 2021-08-29 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0014_alter_graduado_n_cursos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduado',
            name='trabaja',
            field=models.CharField(blank=True, choices=[('Si', 'Si'), ('No', 'No')], max_length=10, null=True),
        ),
    ]