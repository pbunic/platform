# Generated by Django 4.2 on 2023-11-04 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_footer_template_body_footer_template_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='template_title',
            field=models.CharField(max_length=100),
        ),
    ]
