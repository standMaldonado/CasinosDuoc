# Generated by Django 4.2.1 on 2023-07-08 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_rename_nombre_ciudad_nombre_ciudad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
