# Generated by Django 5.0.6 on 2024-08-06 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0004_auto_20240806_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='object_id',
        ),
    ]