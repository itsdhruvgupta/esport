# Generated by Django 3.2.4 on 2021-07-22 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='members',
        ),
        migrations.AddField(
            model_name='registration',
            name='members',
            field=models.CharField(default='', max_length=2),
        ),
    ]
