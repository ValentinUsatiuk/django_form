# Generated by Django 4.2.4 on 2023-08-27 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='form',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
