# Generated by Django 5.1.3 on 2024-11-18 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generales', '0007_usuario_usunom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='genero',
            field=models.CharField(choices=[('m', 'M'), ('f', 'F'), ('o', 'Otro'), ('prefiero_no_decirlo', 'Prefiero no decirlo')], default='prefiero_no_decirlo', max_length=20),
        ),
    ]