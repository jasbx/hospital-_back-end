# Generated by Django 5.0.1 on 2024-01-14 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_rename_date_hospital_manage_data_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital_manage',
            old_name='name',
            new_name='name1',
        ),
    ]
