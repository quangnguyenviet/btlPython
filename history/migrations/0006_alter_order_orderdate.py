# Generated by Django 5.1 on 2024-10-10 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0005_alter_order_orderdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderDate',
            field=models.CharField(default='2024-10-10 21:22:07', max_length=19),
        ),
    ]
