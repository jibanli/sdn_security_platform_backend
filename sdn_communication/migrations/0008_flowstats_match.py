# Generated by Django 2.2.1 on 2019-08-16 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdn_communication', '0007_auto_20190815_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowstats',
            name='match',
            field=models.CharField(default='', max_length=50),
        ),
    ]
