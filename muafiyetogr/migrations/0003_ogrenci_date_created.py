# Generated by Django 2.0.4 on 2018-04-22 16:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('muafiyetogr', '0002_auto_20180422_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='ogrenci',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]