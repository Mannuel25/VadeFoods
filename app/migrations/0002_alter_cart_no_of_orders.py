# Generated by Django 4.2.1 on 2023-09-07 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='no_of_orders',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
