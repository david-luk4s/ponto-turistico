# Generated by Django 3.0.2 on 2020-02-07 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource_tourist', '0002_auto_20200124_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcetourist',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='resource_tourist'),
        ),
    ]
