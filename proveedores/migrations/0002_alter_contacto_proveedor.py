# Generated by Django 4.2.4 on 2023-08-27 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proveedores.proveedor'),
        ),
    ]