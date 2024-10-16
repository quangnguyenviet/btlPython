# Generated by Django 5.1 on 2024-10-11 08:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('paymentID', models.AutoField(primary_key=True, serialize=False)),
                ('paymentDate', models.CharField(default='2024-10-11 15:55:38', max_length=19)),
                ('paymentMethod', models.CharField(choices=[('Credit Card', 'Credit Card'), ('COD', 'COD')], default='Credit Card', max_length=12)),
                ('paymentStatus', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=10)),
                ('order', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='history.order')),
            ],
            options={
                'db_table': 'payment',
            },
        ),
    ]
