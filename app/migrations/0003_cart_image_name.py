# Generated by Django 4.2.1 on 2023-09-07 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_cart_no_of_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='image_name',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
