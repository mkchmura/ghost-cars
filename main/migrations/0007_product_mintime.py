# Generated by Django 2.0 on 2024-02-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20240219_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mintime',
            field=models.IntegerField(default=0),
        ),
    ]
