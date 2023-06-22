# Generated by Django 4.2.1 on 2023-06-17 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('barberia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('usuario',),
            },
        ),
        migrations.CreateModel(
            name='Megusta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_me_gusta', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('usuario',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('barberia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barberia.barberia')),
            ],
            options={
                'ordering': ('barberia',),
            },
        ),
    ]
