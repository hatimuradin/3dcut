# Generated by Django 3.1.1 on 2020-11-10 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20201110_1158'),
        ('cart', '0004_auto_20201107_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='metal_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.metal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='shape_length',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
