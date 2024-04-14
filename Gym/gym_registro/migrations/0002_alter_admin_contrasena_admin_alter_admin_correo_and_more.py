# Generated by Django 5.0.2 on 2024-04-14 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_registro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='contrasena_admin',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='admin',
            name='correo',
            field=models.EmailField(max_length=20),
        ),
        migrations.AlterField(
            model_name='admin',
            name='direccion',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='admin',
            name='documento',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='admin',
            name='identificacion_propietario',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='admin',
            name='telefono',
            field=models.CharField(max_length=10),
        ),
    ]
