# Generated by Django 4.2.1 on 2023-06-18 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='age',
        ),
        migrations.AddField(
            model_name='customuser',
            name='es_profesional',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='es_propietario',
            field=models.BooleanField(default=False),
        ),
    ]
