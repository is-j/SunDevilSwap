# Generated by Django 5.1.3 on 2024-12-07 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
