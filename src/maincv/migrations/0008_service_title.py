# Generated by Django 2.0.2 on 2018-10-31 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maincv', '0007_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Service Title'),
        ),
    ]