# Generated by Django 5.0 on 2023-12-17 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_rename_image2_productimage_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='availability',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
