# Generated by Django 4.2 on 2023-11-15 20:46

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_alter_techstack_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeLab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('lab_image_one', models.ImageField(help_text='Homelab cover image.', upload_to='homelab-cover/')),
                ('lab_image_two', models.ImageField(help_text='Homelab cover image.', upload_to='homelab-cover/')),
                ('lab_image_three', models.ImageField(help_text='Homelab cover image.', upload_to='homelab-cover/')),
            ],
            options={
                'verbose_name_plural': 'Homelab informations',
            },
        ),
        migrations.CreateModel(
            name='HomeLabElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(choices=[('ICT', 'INFRASTRUCTURE'), ('IOT', 'INTERNET-OF-THINGS'), ('SBC', 'SINGLE-BOARD-COMPUTERS'), ('RFD', 'RADIO-FREQUENCY'), ('ACC', 'ACCESSORIES')], max_length=3)),
                ('wide_image', models.ImageField(help_text='Wide - 900x300.', upload_to='homelab/')),
                ('narrow_image', models.ImageField(help_text='Narrow - 500x500.', upload_to='homelab/')),
                ('body', mdeditor.fields.MDTextField()),
            ],
            options={
                'verbose_name_plural': 'Homelab hardware pieces',
                'ordering': ['-date'],
            },
        ),
        migrations.AlterModelOptions(
            name='footer',
            options={'ordering': ['link_section'], 'verbose_name_plural': 'Footer links'},
        ),
        migrations.RemoveIndex(
            model_name='footer',
            name='blog_footer_link_se_c44637_idx',
        ),
        migrations.AddIndex(
            model_name='footer',
            index=models.Index(fields=['link_section'], name='blog_footer_link_se_503877_idx'),
        ),
        migrations.AddIndex(
            model_name='homelabelement',
            index=models.Index(fields=['-date'], name='blog_homela_date_ffce91_idx'),
        ),
    ]
