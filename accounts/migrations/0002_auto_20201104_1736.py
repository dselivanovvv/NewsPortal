# Generated by Django 3.1.2 on 2020-11-04 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(upload_to='profile_photos'),
        ),
    ]