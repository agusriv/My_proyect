# Generated by Django 4.1.2 on 2022-11-14 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_persona'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntegrantesEmpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
            ],
        ),
    ]