# Generated by Django 3.0.4 on 2020-03-30 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FuncionesBasicas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='nombre',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]