# Generated by Django 3.1.1 on 2020-11-21 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20201117_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='metal',
            name='max_length',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='metal',
            name='min_length',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]