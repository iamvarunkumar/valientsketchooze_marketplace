# Generated by Django 5.1.7 on 2025-03-29 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_alter_artwork_options_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='provider_order_id',
            field=models.CharField(help_text='Razorpay Order ID', max_length=40),
        ),
    ]
