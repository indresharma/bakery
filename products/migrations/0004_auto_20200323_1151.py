# Generated by Django 3.0.2 on 2020-03-23 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200321_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Dry cakes', 'Dry Cakes'), ('Cakes', 'Cakes'), ('Cookies', 'Cookies')], max_length=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='label',
            field=models.CharField(choices=[('danger', 'danger'), ('secondary', 'secondary'), ('primary', 'primary')], max_length=15),
        ),
    ]