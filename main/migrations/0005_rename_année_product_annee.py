# Generated by Django 4.2.3 on 2023-07-10 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_product_marque"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="année",
            new_name="annee",
        ),
    ]
