# Generated by Django 2.0.2 on 2018-07-05 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maincv', '0005_education_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='profile',
            name='quote',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Quote'),
        ),
    ]