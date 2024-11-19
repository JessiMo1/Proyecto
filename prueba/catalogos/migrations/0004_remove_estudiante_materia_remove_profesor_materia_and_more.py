# Generated by Django 5.1.3 on 2024-11-18 21:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0003_aula_materia_fechahora_materia_aula_profesor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='materia',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='materia',
        ),
        migrations.AlterField(
            model_name='profesor',
            name='aula',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogos.aula'),
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('fechahora', models.DateTimeField(auto_now_add=True, null=True)),
                ('aula', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogos.aula')),
            ],
        ),
        migrations.AddField(
            model_name='estudiante',
            name='clase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogos.clase'),
        ),
        migrations.AddField(
            model_name='profesor',
            name='clase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogos.clase'),
        ),
        migrations.DeleteModel(
            name='Materia',
        ),
    ]