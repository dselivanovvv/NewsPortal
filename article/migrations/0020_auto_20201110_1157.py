# Generated by Django 3.1.3 on 2020-11-10 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0019_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='article_images'),
        ),
    ]
