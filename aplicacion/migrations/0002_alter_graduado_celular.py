# Generated by Django 3.2.3 on 2021-08-18 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduado',
            name='celular',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Celular'),
        ),
    ]