# Generated by Django 2.2.2 on 2019-07-01 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mdesigner', '0005_auto_20190630_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mdesigner.Usuario'),
        ),
    ]
