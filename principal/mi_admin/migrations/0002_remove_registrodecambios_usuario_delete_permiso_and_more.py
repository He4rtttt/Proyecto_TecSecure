# Generated by Django 5.0.4 on 2024-04-12 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mi_admin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrodecambios',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Permiso',
        ),
        migrations.DeleteModel(
            name='RegistroDeCambios',
        ),
    ]