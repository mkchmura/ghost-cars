# Generated by Django 2.0 on 2024-02-19 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_année_product_annee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price48',
            new_name='franchiseabo',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price72',
            new_name='price24abo',
        ),
        migrations.RemoveField(
            model_name='product',
            name='annee',
        ),
        migrations.RemoveField(
            model_name='product',
            name='autonomie',
        ),
        migrations.RemoveField(
            model_name='product',
            name='bagages',
        ),
        migrations.RemoveField(
            model_name='product',
            name='places',
        ),
        migrations.RemoveField(
            model_name='product',
            name='vitessemax',
        ),
        migrations.AddField(
            model_name='product',
            name='bookable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='future',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='price7',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='product',
            name='price7abo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default='static/img/token.png', help_text='Upload a product image', upload_to='static/img/', verbose_name='image'),
        ),
    ]
