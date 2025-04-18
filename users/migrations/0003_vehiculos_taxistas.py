# Generated by Django 5.2 on 2025-04-16 02:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_usuarios_identificion_usuarios_identificacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=15)),
                ('modelo', models.IntegerField()),
                ('marca', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Taxistas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=150)),
                ('numero_licencia', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.vehiculos')),
            ],
        ),
    ]
