# Generated by Django 3.1.1 on 2020-11-10 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20201110_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='old_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sku',
        ),
        migrations.AlterField(
            model_name='metal',
            name='name',
            field=models.CharField(default='aluminum6610', max_length=255, unique=True),
        ),
    ]
