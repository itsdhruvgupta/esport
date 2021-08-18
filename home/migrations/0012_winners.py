# Generated by Django 3.2.4 on 2021-06-15 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210612_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='winners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=50)),
                ('player_profile', models.ImageField(upload_to='static/')),
                ('game', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=50)),
            ],
        ),
    ]