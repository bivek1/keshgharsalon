# Generated by Django 3.0.3 on 2020-07-24 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppKesh', '0011_stafflist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stafflist',
            name='staffnumber',
            field=models.CharField(max_length=200),
        ),
    ]