# Generated by Django 5.1.2 on 2024-11-19 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mhs_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='product',
            new_name='product_id',
        ),
    ]
