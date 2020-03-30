# Generated by Django 3.0.4 on 2020-03-30 01:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('codigo', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('nombreEmpresa', models.CharField(max_length=80)),
                ('celular', models.CharField(max_length=8)),
                ('emailEmpresa', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('codigo', models.CharField(max_length=120)),
                ('fechaNac', models.DateField()),
                ('genero', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='TelefonosEmpleados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telf', models.CharField(max_length=8)),
                ('llaveForanea', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.Empleados')),
            ],
        ),
        migrations.CreateModel(
            name='TelefonosEmpleadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telf', models.CharField(max_length=8)),
                ('llaveForanea', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.Empleadores')),
            ],
        ),
        migrations.CreateModel(
            name='TarjetaTrabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempoDisponible', models.IntegerField()),
                ('zona', models.CharField(max_length=200)),
                ('llaveForanea', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.Empleados')),
            ],
        ),
        migrations.CreateModel(
            name='TagBusqueda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=30)),
                ('llaveForanea', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.TarjetaTrabajo')),
            ],
        ),
        migrations.CreateModel(
            name='historialCreacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaCreacion', models.DateTimeField(default=datetime.date.today)),
                ('llaveForaneaEmpleados', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.Empleados')),
                ('llaveForaneaTarjeta', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.TarjetaTrabajo')),
            ],
        ),
        migrations.CreateModel(
            name='historialConsulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaConsulta', models.DateTimeField(default=datetime.date.today)),
                ('llaveForaneaEmpleadores', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.Empleadores')),
                ('llaveForaneaTarjeta', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.TarjetaTrabajo')),
            ],
        ),
        migrations.CreateModel(
            name='EmailRefetenceiaEmpleados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('llaveForanea', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.Empleados')),
            ],
        ),
        migrations.CreateModel(
            name='DireccionEmpleadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=200)),
                ('llaveForanea', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.Empleadores')),
            ],
        ),
    ]
