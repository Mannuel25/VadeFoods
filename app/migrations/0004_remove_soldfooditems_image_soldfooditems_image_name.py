# Generated by Django 4.2.1 on 2023-09-07 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_cart_image_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soldfooditems',
            name='image',
        ),
        migrations.AddField(
            model_name='soldfooditems',
            name='image_name',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
