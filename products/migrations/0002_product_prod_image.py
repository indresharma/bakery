# Generated by Django 3.0.2 on 2020-01-16 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prod_image',
            field=models.CharField(default='https://s3.amazonaws.com/ODNUploads/563be68403b50placeholder_food_item_2.png', max_length=500),
        ),
    ]
