# Generated by Django 5.1.3 on 2024-11-18 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generales', '0010_alter_usuario_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='genero',
            field=models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer'), ('Otro', 'Otro'), ('prefiero_no_decirlo', 'Prefiero no decirlo')], default='prefiero_no_decirlo', max_length=20),
        ),
    ]
