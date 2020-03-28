# Generated by Django 3.0.4 on 2020-03-25 22:49

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
                ('Nombre', models.CharField(max_length=80)),
                ('codigo', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
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
            name='TarjetaTrabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('llaveForaneaEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.Empleados')),
                ('llaveForaneaEmpleador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.Empleadores')),
            ],
        ),
        migrations.CreateModel(
            name='ZonaTrabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zona', models.CharField(max_length=200)),
                ('llaveForanea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.TarjetaTrabajo')),
            ],
        ),
        migrations.CreateModel(
            name='TiempoDisponible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempoDisponoble', models.IntegerField()),
                ('llaveForania', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.TarjetaTrabajo')),
            ],
        ),
        migrations.CreateModel(
            name='TelefonosEmpleados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telf', models.CharField(max_length=8)),
                ('llaveForanea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.Empleados')),
            ],
        ),
        migrations.CreateModel(
            name='TelefonosEmpleadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elf', models.CharField(max_length=8)),
                ('llaveForanea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.Empleadores')),
            ],
        ),
        migrations.CreateModel(
            name='TagBusqueda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=30)),
                ('llaveForanea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.TarjetaTrabajo')),
            ],
        ),
        migrations.CreateModel(
            name='historialCreacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaCreacion', models.DateTimeField()),
                ('llaveForaneaEmpleados', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.Empleados')),
                ('llaveForaneaTarjeta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.TarjetaTrabajo')),
            ],
        ),
        migrations.CreateModel(
            name='historialConsulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaConsulta', models.DateTimeField()),
                ('llaveForaneaEmpleados', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.Empleados')),
                ('llaveForaneaTarjeta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.TarjetaTrabajo')),
            ],
        ),
        migrations.CreateModel(
            name='EmailRefetenceiaEmpleados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('llaveForanea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.Empleados')),
            ],
        ),
        migrations.CreateModel(
            name='DireccionEmpleadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Direccion', models.CharField(max_length=200)),
                ('llaveForanea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.Empleadores')),
            ],
        ),
    ]
