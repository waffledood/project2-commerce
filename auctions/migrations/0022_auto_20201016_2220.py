# Generated by Django 3.1 on 2020-10-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_auto_20201016_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='listing',
            field=models.IntegerField(default=1, max_length=3),
            preserve_default=False,
        ),
    ]