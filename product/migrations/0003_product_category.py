# Generated by Django 3.2.7 on 2022-05-23 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_category_newproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
