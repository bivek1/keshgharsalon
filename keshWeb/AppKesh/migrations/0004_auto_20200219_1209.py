# Generated by Django 3.0.3 on 2020-02-19 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppKesh', '0003_productadding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productadding',
            name='product_price',
            field=models.IntegerField(default=0),
        ),
    ]
