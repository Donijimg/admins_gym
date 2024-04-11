# Generated by Django 5.0.2 on 2024-04-11 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_registro', '0003_alter_clientroutine_estatura_alter_clientroutine_imc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='documento',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='admin',
            name='identificacion_propietario',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='admin',
            name='nombre_admin',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='coach',
            name='documento',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='documento',
            field=models.IntegerField(max_length=10),
        ),
    ]
