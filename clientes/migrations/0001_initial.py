# Generated by Django 4.1 on 2022-08-17 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellidos', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
    ]
