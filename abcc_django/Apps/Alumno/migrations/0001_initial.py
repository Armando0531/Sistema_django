# Generated by Django 5.0.4 on 2024-04-19 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numcontrol', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('semestre', models.IntegerField()),
            ],
        ),
    ]