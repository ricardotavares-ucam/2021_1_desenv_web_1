# Generated by Django 3.2 on 2021-05-26 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
