# Generated by Django 4.2.7 on 2024-02-03 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category_remove_blog_date_blog_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
