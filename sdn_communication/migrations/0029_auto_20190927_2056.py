# Generated by Django 2.2.1 on 2019-09-27 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdn_communication', '0028_auto_20190927_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switch',
            name='switch_number',
            field=models.IntegerField(default=-1),
        ),
    ]
