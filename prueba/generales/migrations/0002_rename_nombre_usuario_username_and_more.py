# Generated by Django 5.1.3 on 2024-11-17 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generales', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='nombre',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='apMaterno',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='apPaterno',
        ),
    ]