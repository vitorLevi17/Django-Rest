# Generated by Django 5.0.7 on 2024-07-24 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_matricula'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matricula',
            old_name='Perdiodo',
            new_name='periodo',
        ),
    ]