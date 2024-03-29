# Generated by Django 5.0.1 on 2024-02-20 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_rename_hospital_manage_login_delete_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search_doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='photo')),
                ('name', models.CharField(max_length=50)),
                ('specialization', models.CharField(max_length=50)),
                ('day_in', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='login',
            name='name1',
            field=models.CharField(max_length=100),
        ),
    ]
