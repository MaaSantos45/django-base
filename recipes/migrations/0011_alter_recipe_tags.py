# Generated by Django 5.0.6 on 2024-08-06 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_recipe_tags'),
        ('tags', '0005_remove_tag_content_type_remove_tag_object_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='recipes', to='tags.tag'),
        ),
    ]