# Generated by Django 3.1 on 2020-10-11 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auction_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='bid',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
