# Generated by Django 3.1.1 on 2020-11-13 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20201110_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='CircularItem',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cart.item')),
                ('bar_length', models.IntegerField()),
                ('radius', models.IntegerField()),
            ],
            bases=('cart.item',),
        ),
        migrations.CreateModel(
            name='RectangularItem',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cart.item')),
            ],
            bases=('cart.item',),
        ),
        migrations.RemoveField(
            model_name='item',
            name='shape_length',
        ),
    ]
