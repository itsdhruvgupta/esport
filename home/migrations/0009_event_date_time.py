# Generated by Django 3.2.4 on 2021-06-10 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_event_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
