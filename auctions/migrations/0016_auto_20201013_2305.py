# Generated by Django 3.1 on 2020-10-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auto_20201011_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='category',
            field=models.CharField(choices=[('Books', 'Books'), ('Automobile', 'Automobile'), ('Toys', 'Toys'), ('Food', 'Food'), ('Clothing', 'Clothing'), ('Others', 'Others')], default='Others', max_length=32),
        ),
    ]
