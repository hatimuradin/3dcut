# Generated by Django 3.1.1 on 2020-11-17 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20201110_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cross_section',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]
