# Generated by Django 2.2.1 on 2019-08-16 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdn_communication', '0011_auto_20190816_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='portstats',
            name='port',
            field=models.IntegerField(default=0),
        ),
    ]
