# Generated by Django 4.2.1 on 2023-06-21 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, default='images/post/default_image.jpg', null=True, upload_to='images/post'),
        ),
    ]
