# Generated by Django 5.2 on 2025-05-18 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_metodopago_perfilusuario_viaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metodopago',
            name='tipo',
            field=models.CharField(choices=[('credito', 'Tarjeta de Crédito'), ('debito', 'Tarjeta Débito'), ('efectivo', 'Efectivo'), ('nequi', 'Nequi'), ('daviplata', 'Daviplata')], max_length=50),
        ),
    ]
