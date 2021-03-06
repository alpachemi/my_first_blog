# Generated by Django 2.0.2 on 2018-03-24 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.UUIDField(help_text='Id para un usuario', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=150)),
                ('fecha_nacimiento', models.DateTimeField(blank=True, null=True)),
                ('telefono_1', models.CharField(max_length=15)),
                ('telefono_2', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=40)),
                ('localidad', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=100)),
                ('codigo_postal', models.CharField(max_length=10)),
                ('sexo', models.CharField(max_length=1)),
                ('carne_conducir', models.BooleanField(default=False)),
                ('cuidador', models.BooleanField(default=False)),
                ('administrador', models.BooleanField(default=False)),
            ],
        ),
    ]
