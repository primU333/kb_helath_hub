# Generated by Django 4.2.7 on 2023-11-23 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_Us_Page_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us_title_sub_text', models.TextField()),
                ('about_us_introduction_title', models.CharField(max_length=200)),
                ('about_us_introduction_subtext', models.TextField()),
                ('mission', models.TextField()),
                ('vision', models.TextField()),
                ('goal', models.TextField()),
                ('about_us_objectives_image', models.ImageField(upload_to='settings')),
                ('consultation_sub_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Advice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advice', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Contact_Us_Page_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_us_title_sub_text', models.TextField()),
                ('map_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Home_Page_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_page_main_image', models.ImageField(default='default.jpg', upload_to='settings')),
                ('home_page_main_title', models.CharField(max_length=200)),
                ('home_page_intro_title', models.CharField(max_length=200)),
                ('home_page_sub_title', models.TextField()),
                ('home_page_intro_image1', models.ImageField(default='default.jpg', upload_to='settings')),
                ('home_page_intro_image2', models.ImageField(default='default.jpg', upload_to='settings')),
                ('advice_title', models.CharField(max_length=200)),
                ('advice_sub_text', models.TextField()),
                ('prevention_title', models.CharField(max_length=200)),
                ('prevention_sub_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Home_Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_cases', models.IntegerField(default=0)),
                ('recovered_cases', models.IntegerField(default=0)),
                ('death_cases', models.IntegerField(default=0)),
                ('treated_cases', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Prevention_Method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method_name', models.CharField(max_length=30)),
                ('method_image', models.ImageField(upload_to='prevention_methods')),
                ('method_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Team_Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('linkedin_link', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='team')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimony', models.TextField()),
                ('submited_by_name', models.CharField(max_length=100)),
                ('submited_by_image', models.ImageField(default='default.jpg', upload_to='testionials')),
            ],
        ),
    ]
