# Generated by Django 4.2.3 on 2023-07-20 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='imagen',
            field=models.ImageField(blank=True, default='usuarios/usuarios_def.png', null=True, upload_to='usuarios'),
        ),
    ]