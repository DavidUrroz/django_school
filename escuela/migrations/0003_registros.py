# Generated by Django 4.2.4 on 2023-09-14 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0002_salon_codigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='PDFs')),
            ],
        ),
    ]