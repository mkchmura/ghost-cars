# Generated by Django 4.2.3 on 2023-07-10 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productimage",
            options={
                "verbose_name": "Product Image",
                "verbose_name_plural": "Product Images",
            },
        ),
        migrations.RemoveField(
            model_name="product",
            name="author",
        ),
        migrations.RemoveField(
            model_name="product",
            name="created_by",
        ),
        migrations.RemoveField(
            model_name="product",
            name="description",
        ),
        migrations.RemoveField(
            model_name="product",
            name="price",
        ),
        migrations.RemoveField(
            model_name="productimage",
            name="is_main",
        ),
        migrations.AddField(
            model_name="product",
            name="année",
            field=models.CharField(default="none", max_length=255),
        ),
        migrations.AddField(
            model_name="product",
            name="autonomie",
            field=models.CharField(default="none", max_length=255),
        ),
        migrations.AddField(
            model_name="product",
            name="bagages",
            field=models.CharField(default="none", max_length=255),
        ),
        migrations.AddField(
            model_name="product",
            name="franchise",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name="product",
            name="kmsupp",
            field=models.CharField(default="none", max_length=255),
        ),
        migrations.AddField(
            model_name="product",
            name="places",
            field=models.CharField(default="none", max_length=255),
        ),
        migrations.AddField(
            model_name="product",
            name="price24",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name="product",
            name="price48",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name="product",
            name="price72",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name="product",
            name="vitessemax",
            field=models.CharField(default="none", max_length=255),
        ),
        migrations.AddField(
            model_name="productimage",
            name="alt_text",
            field=models.CharField(
                blank=True,
                help_text="Write an Alt",
                max_length=255,
                null=True,
                verbose_name="Alternativee text",
            ),
        ),
        migrations.AddField(
            model_name="productimage",
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="productimage",
            name="is_feature",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="productimage",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="slug",
            field=models.SlugField(default="none", max_length=255),
        ),
        migrations.AlterField(
            model_name="product",
            name="title",
            field=models.CharField(default="none", max_length=255),
        ),
        migrations.AlterField(
            model_name="productimage",
            name="image",
            field=models.ImageField(
                default="img/token.png",
                help_text="Upload a product image",
                upload_to="img/",
                verbose_name="image",
            ),
        ),
        migrations.AlterField(
            model_name="productimage",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_image",
                to="main.product",
            ),
        ),
    ]
