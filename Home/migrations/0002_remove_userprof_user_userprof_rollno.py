# Generated by Django 4.1.4 on 2023-01-01 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprof',
            name='User',
        ),
        migrations.AddField(
            model_name='userprof',
            name='RollNo',
            field=models.IntegerField(default=69),
        ),
    ]
