# Generated by Django 5.1.7 on 2025-03-29 06:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artwork',
            options={},
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('PAID', 'Paid'), ('FAILED', 'Failed')], default='PENDING', max_length=10)),
                ('provider_order_id', models.CharField(help_text='Razorpay Order ID', max_length=40, unique=True)),
                ('payment_id', models.CharField(blank=True, help_text='Razorpay Payment ID', max_length=40, null=True)),
                ('signature', models.CharField(blank=True, help_text='Razorpay Signature', max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='marketplace.artwork')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
