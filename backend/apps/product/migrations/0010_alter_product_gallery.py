# Generated by Django 3.2.8 on 2023-10-02 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_category_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gallery',
            field=models.ManyToManyField(blank=True, null=True, to='product.ProductGallery'),
        ),
    ]
