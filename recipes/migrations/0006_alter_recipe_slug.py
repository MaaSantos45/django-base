# Generated by Django 5.0.6 on 2024-07-10 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_category_name_alter_recipe_is_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(max_length=70, unique=True),
        ),
    ]
