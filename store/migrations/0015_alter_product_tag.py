# Generated by Django 4.2.5 on 2023-09-16 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_alter_product_created_at_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.CharField(max_length=150, verbose_name='商品標籤'),
        ),
    ]
