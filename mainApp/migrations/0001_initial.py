# Generated by Django 5.1.4 on 2024-12-06 01:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemID', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cloth', models.BooleanField(default=False)),
                ('equip', models.BooleanField(default=False)),
                ('text', models.BooleanField(default=False)),
                ('condition', models.CharField(choices=[('New', 'New'), ('Used', 'Used')], max_length=100)),
                ('image', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cloth', models.BooleanField(default=False)),
                ('equip', models.BooleanField(default=False)),
                ('condition', models.CharField(choices=[('New', 'New'), ('Used', 'Used')], max_length=100)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='filter', to='mainApp.item')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to='mainApp.user')),
                ('logout', models.BooleanField(default=False)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='login', to='mainApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment', models.CharField(choices=[('Completed', 'Completed'), ('NoPayment', 'NoPayment')], max_length=255)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_entries', to='mainApp.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='mainApp.user')),
            ],
        ),
    ]