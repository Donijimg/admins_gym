# Generated by Django 5.0.2 on 2024-04-16 18:42

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
                ('especializacion', models.CharField(max_length=30)),
                ('horarios', models.CharField(max_length=30)),
                ('typo_id', models.IntegerField(choices=[(1, 'Fitness'), (2, 'Pilates')])),
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
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrenador', models.ManyToManyField(blank=True, related_name='inscripciones', to='gym_registro.coach')),
                ('usuario', models.ManyToManyField(blank=True, related_name='inscripciones', to='gym_registro.user')),
            ],
        ),
    ]
