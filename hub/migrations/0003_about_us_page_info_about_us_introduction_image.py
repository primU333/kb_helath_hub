# Generated by Django 4.2.7 on 2023-11-24 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0002_home_page_info_home_page_intro_sub_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_us_page_info',
            name='about_us_introduction_image',
            field=models.ImageField(default='default.jpg', upload_to='settings'),
        ),
    ]