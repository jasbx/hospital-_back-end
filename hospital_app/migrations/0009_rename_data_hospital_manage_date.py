# Generated by Django 5.0.1 on 2024-01-13 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_hospital_manage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital_manage',
            old_name='data',
            new_name='date',
        ),
    ]
