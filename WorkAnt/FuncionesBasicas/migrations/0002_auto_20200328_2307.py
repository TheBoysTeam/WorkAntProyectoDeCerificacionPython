# Generated by Django 3.0.4 on 2020-03-28 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FuncionesBasicas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccionempleadores',
            name='llaveForanea',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.Empleadores'),
        ),
        migrations.AlterField(
            model_name='emailrefetenceiaempleados',
            name='llaveForanea',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.Empleados'),
        ),
        migrations.AlterField(
            model_name='historialconsulta',
            name='llaveForaneaEmpleadores',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.Empleadores'),
        ),
        migrations.AlterField(
            model_name='historialconsulta',
            name='llaveForaneaTarjeta',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.TarjetaTrabajo'),
        ),
        migrations.AlterField(
            model_name='historialcreacion',
            name='llaveForaneaEmpleados',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.Empleados'),
        ),
        migrations.AlterField(
            model_name='historialcreacion',
            name='llaveForaneaTarjeta',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.TarjetaTrabajo'),
        ),
        migrations.AlterField(
            model_name='tagbusqueda',
            name='llaveForanea',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.TarjetaTrabajo'),
        ),
        migrations.AlterField(
            model_name='tarjetatrabajo',
            name='llaveForanea',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.Empleados'),
        ),
        migrations.AlterField(
            model_name='telefonosempleadores',
            name='llaveForanea',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.Empleadores'),
        ),
        migrations.AlterField(
            model_name='telefonosempleados',
            name='llaveForanea',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='FuncionesBasicas.Empleados'),
        ),
    ]
