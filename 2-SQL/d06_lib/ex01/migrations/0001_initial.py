# Generated by Django 5.0 on 2023-12-12 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('title', models.CharField(max_length=64)),
                ('episode_nb', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('opening_crawl', models.TextField(null=True)),
                ('director', models.TextField(max_length=32)),
                ('producer', models.TextField(max_length=128)),
            ],
        ),
    ]
