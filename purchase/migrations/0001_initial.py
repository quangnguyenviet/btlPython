# Generated by Django 5.1 on 2024-10-09 07:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('productDetail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderID', models.AutoField(primary_key=True, serialize=False)),
                ('orderDate', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shippingAddress', models.CharField(max_length=255)),
                ('itemQuantity', models.PositiveIntegerField(default=1)),
                ('orderStatus', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=10)),
                ('itemID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productDetail.item')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('paymentID', models.AutoField(primary_key=True, serialize=False)),
                ('paymentDate', models.DateTimeField(auto_now_add=True)),
                ('paymentMethod', models.CharField(max_length=50)),
                ('paymentStatus', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=10)),
                ('orderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.order')),
            ],
        ),
    ]
