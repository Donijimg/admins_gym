# Generated by Django 5.0.2 on 2024-04-17 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion_propietario', models.CharField(blank=True, max_length=20, null=True)),
                ('documento', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('nombre_admin', models.CharField(max_length=50)),
                ('apellido_admin', models.CharField(max_length=50)),
                ('contrasena_admin', models.CharField(max_length=128)),
                ('correo', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('correo', models.EmailField(max_length=100)),
                ('experiencia', models.IntegerField(blank=True, null=True)),
                ('contrasena', models.CharField(max_length=128)),
                ('ficha_de_ingreso', models.CharField(max_length=10)),
                ('genero', models.CharField(max_length=10)),
                ('horarios', models.CharField(max_length=30)),
                ('typo_id', models.IntegerField(blank=True, choices=[(1, 'Fitness'), (2, 'Pilates'), (3, 'Rehabilitacion fisica'), (4, 'Plan para mayores'), (5, 'Yoga'), (6, 'Gimnasia')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudesCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('estatura', models.DecimalField(blank=True, decimal_places=2, max_digits=4)),
                ('objetivos', models.TextField(blank=True)),
                ('correo', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=10)),
                ('edad', models.IntegerField()),
                ('telefono', models.CharField(max_length=15)),
                ('contrasena', models.CharField(max_length=128)),
                ('correo', models.EmailField(max_length=100)),
            ],
        ),
    ]
