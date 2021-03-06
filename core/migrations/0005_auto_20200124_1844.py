# Generated by Django 3.0.2 on 2020-01-24 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
        ('resource_tourist', '0002_auto_20200124_1844'),
        ('core', '0004_touristpoint_resource_tourist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='touristpoint',
            name='resource_tourist',
        ),
        migrations.AddField(
            model_name='touristpoint',
            name='comments',
            field=models.ManyToManyField(to='comment.Comment'),
        ),
        migrations.AddField(
            model_name='touristpoint',
            name='resource_tourists',
            field=models.ManyToManyField(to='resource_tourist.ResourceTourist'),
        ),
        migrations.AlterField(
            model_name='touristpoint',
            name='date_register',
            field=models.DateField(auto_now_add=True),
        ),
    ]
