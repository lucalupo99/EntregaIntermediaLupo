# Generated by Django 4.1 on 2022-12-01 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Peluqueria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_deseada', models.CharField(max_length=50)),
                ('Telefono', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='turnos',
            name='fecha_deseada',
            field=models.CharField(max_length=50),
        ),
    ]
