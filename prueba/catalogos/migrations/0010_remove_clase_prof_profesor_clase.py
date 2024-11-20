# Generated by Django 5.1.3 on 2024-11-19 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0009_remove_asistencia_estudiante_remove_profesor_clase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clase',
            name='prof',
        ),
        migrations.AddField(
            model_name='profesor',
            name='clase',
            field=models.ManyToManyField(null=True, related_name='profesores', to='catalogos.clase'),
        ),
    ]