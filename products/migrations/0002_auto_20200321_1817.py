# Generated by Django 3.0.2 on 2020-03-21 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='txt'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Dry cakes', 'Dry Cakes'), ('Cakes', 'Cakes'), ('Cookies', 'Cookies')], max_length=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='label',
            field=models.CharField(choices=[('secondary', 'secondary'), ('danger', 'danger'), ('primary', 'primary')], max_length=15),
        ),
    ]
