# Generated by Django 5.0.7 on 2024-07-29 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_rename_perdiodo_matricula_periodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudantes',
            name='CPF',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
