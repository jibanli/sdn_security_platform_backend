# Generated by Django 2.2.1 on 2019-09-29 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdn_communication', '0027_auto_20190928_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='attacknotification',
            name='attack_value',
            field=models.IntegerField(default=-1),
        ),
    ]