# Generated by Django 3.0.5 on 2020-04-26 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200426_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photo/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnailimage',
            field=models.ImageField(upload_to='thumbnail/'),
        ),
    ]
