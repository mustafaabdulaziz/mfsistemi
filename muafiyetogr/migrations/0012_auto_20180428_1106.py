# Generated by Django 2.0.4 on 2018-04-28 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muafiyetogr', '0011_onayformu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onayformu',
            name='OnayDurumu',
            field=models.CharField(choices=[('onay', 'onay'), ('Red', 'Red'), ('bekleniyor', 'bekleniyor')], default='bekleniyor', max_length=6),
        ),
    ]
