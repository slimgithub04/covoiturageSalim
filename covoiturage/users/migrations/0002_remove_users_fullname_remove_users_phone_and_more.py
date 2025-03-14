# Generated by Django 4.2 on 2024-11-09 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='users',
            name='phone',
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(default='default@gmail.com', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(default='Utilisateur', max_length=15),
        ),
    ]
