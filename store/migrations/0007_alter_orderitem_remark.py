# Generated by Django 4.2.5 on 2023-09-11 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_orderitem_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='remark',
            field=models.TextField(blank=True, null=True),
        ),
    ]