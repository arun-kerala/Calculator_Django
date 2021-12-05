# Generated by Django 3.1 on 2021-12-05 14:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculator_histoty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equation', models.CharField(max_length=25)),
                ('result', models.CharField(max_length=25)),
                ('date_added', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]