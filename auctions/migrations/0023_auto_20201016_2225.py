# Generated by Django 3.1 on 2020-10-16 14:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_auto_20201016_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='listing',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
