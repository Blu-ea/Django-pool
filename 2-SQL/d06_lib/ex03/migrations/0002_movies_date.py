# Generated by Django 5.0 on 2023-12-12 15:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex03', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
