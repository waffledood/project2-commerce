# Generated by Django 3.1 on 2020-10-09 15:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auction_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='bidder',
            field=models.ManyToManyField(blank=True, related_name='bidder', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='auction',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
