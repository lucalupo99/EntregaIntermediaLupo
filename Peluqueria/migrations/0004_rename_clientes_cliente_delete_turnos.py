# Generated by Django 4.1 on 2022-12-02 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Peluqueria', '0003_remove_turno_fecha_deseada_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clientes',
            new_name='Cliente',
        ),
        migrations.DeleteModel(
            name='Turnos',
        ),
    ]