# Generated by Django 5.1.3 on 2024-11-17 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generales', '0003_rename_contraseña_usuario_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(help_text='Maximo 128 caracteres', max_length=128),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]
