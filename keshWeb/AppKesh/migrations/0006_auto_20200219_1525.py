# Generated by Django 3.0.3 on 2020-02-19 09:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppKesh', '0005_auto_20200219_1239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailytransactions',
            old_name='charge',
            new_name='service_rate',
        ),
        migrations.AddField(
            model_name='dailytransactions',
            name='date_of_transaction',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productadding',
            name='product_Image',
            field=models.ImageField(blank=True, upload_to='productImage/%Y/%m/%d'),
        ),
    ]
