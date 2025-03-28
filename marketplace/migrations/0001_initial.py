# Generated by Django 5.1.7 on 2025-03-28 16:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title of the artwork.', max_length=200)),
                ('description', models.TextField(blank=True, help_text='A detailed description of the artwork (optional).', null=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Price in INR.', max_digits=10)),
                ('image', models.ImageField(help_text='The main image file for the artwork.', upload_to='artworks/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('artist', models.ForeignKey(help_text='The artist who uploaded this artwork.', on_delete=django.db.models.deletion.CASCADE, related_name='artworks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
