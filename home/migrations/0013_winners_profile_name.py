# Generated by Django 3.2.4 on 2021-06-15 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_winners'),
    ]

    operations = [
        migrations.AddField(
            model_name='winners',
            name='profile_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]