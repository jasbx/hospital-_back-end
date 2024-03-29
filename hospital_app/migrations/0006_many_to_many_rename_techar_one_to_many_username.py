# Generated by Django 5.0.1 on 2024-01-13 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_techar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Many_to_many',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vido', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='Techar',
            new_name='One_to_many',
        ),
        migrations.CreateModel(
            name='Username',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('video', models.ManyToManyField(to='login.many_to_many')),
            ],
        ),
    ]
