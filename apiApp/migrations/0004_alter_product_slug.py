# Generated by Django 5.2.1 on 2025-05-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0003_product_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
