# Generated by Django 2.1.3 on 2018-12-26 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maincv', '0014_testimonial_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_education', models.BooleanField(default=True)),
                ('show_experiences', models.BooleanField(default=True)),
                ('show_testimonials', models.BooleanField(default=True)),
            ],
        ),
    ]
