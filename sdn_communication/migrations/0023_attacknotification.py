# Generated by Django 2.2.1 on 2019-09-16 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdn_communication', '0022_auto_20190916_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttackNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attack_type', models.CharField(default='No Data Yet', max_length=50)),
                ('attack_vector', models.CharField(default='No Data Yet', max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
