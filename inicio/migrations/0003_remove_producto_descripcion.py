# Generated by Django 4.2.6 on 2023-11-18 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_categoria_subcategoria_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='descripcion',
        ),
    ]
