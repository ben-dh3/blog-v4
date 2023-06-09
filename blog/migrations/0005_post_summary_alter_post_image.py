# Generated by Django 4.2 on 2023-07-11 15:17

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(max_length=255, upload_to=blog.models.Post.image_upload_to),
        ),
    ]
