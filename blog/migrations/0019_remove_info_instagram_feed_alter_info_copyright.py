# Generated by Django 4.2 on 2023-11-11 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_info_instagram_feed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='instagram_feed',
        ),
        migrations.AlterField(
            model_name='info',
            name='copyright',
            field=models.CharField(help_text='Bottom copyright text.', max_length=100),
        ),
    ]
