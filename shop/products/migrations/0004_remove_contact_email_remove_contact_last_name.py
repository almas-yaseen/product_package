# Generated by Django 5.0 on 2023-12-17 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_name',
        ),
    ]
