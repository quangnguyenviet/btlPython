# Generated by Django 5.1 on 2024-10-10 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0008_alter_order_orderdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderDate',
            field=models.CharField(default='2024-10-10 14:14:55', max_length=19),
        ),
    ]
