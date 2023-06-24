# Generated by Django 4.2.1 on 2023-06-23 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BEBIDA',
            fields=[
                ('id_bebida', models.AutoField(db_column='IdBebida', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='COMIDA',
            fields=[
                ('id_comida', models.AutoField(db_column='IdComida', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
    ]