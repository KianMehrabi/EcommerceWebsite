# Generated by Django 4.2.15 on 2024-08-28 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_caragory_product_catagory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='catagory',
            new_name='category',
        ),
    ]
