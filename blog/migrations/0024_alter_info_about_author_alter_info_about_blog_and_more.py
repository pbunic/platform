# Generated by Django 4.2 on 2023-12-18 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_delete_homelabelement_alter_homelab_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='about_author',
            field=models.TextField(default='author', help_text='Some informations about author.', max_length=2500),
        ),
        migrations.AlterField(
            model_name='info',
            name='about_blog',
            field=models.TextField(default='blog', help_text='Blog vision and summary.', max_length=2500),
        ),
        migrations.AlterField(
            model_name='info',
            name='base_title',
            field=models.CharField(default='Title', help_text='Navigation spot title.', max_length=30),
        ),
        migrations.AlterField(
            model_name='info',
            name='contact_email',
            field=models.EmailField(default='mail@example.com', help_text='Email for contact.', max_length=254),
        ),
        migrations.AlterField(
            model_name='info',
            name='copyright',
            field=models.CharField(default='(c)', help_text='Bottom copyright text.', max_length=100),
        ),
        migrations.AlterField(
            model_name='info',
            name='home_paragraph',
            field=models.TextField(default='Paragraph', help_text='Landing page short introduction.', max_length=500),
        ),
        migrations.AlterField(
            model_name='info',
            name='home_title',
            field=models.CharField(default='Title', help_text='Landing page title.', max_length=50),
        ),
    ]
