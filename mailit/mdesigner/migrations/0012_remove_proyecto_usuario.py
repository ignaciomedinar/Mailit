# Generated by Django 2.2.2 on 2019-07-02 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mdesigner', '0011_auto_20190701_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='usuario',
        ),
    ]
