# Generated by Django 4.2 on 2023-11-02 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_img_cover_post_imagecover_post_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]