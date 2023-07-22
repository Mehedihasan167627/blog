# Generated by Django 4.2.3 on 2023-07-21 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_home_page_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='is_popular',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='ordering',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
