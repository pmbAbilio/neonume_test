# Generated by Django 3.0.7 on 2020-06-16 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture_displayer', '0004_auto_20200616_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='media/image/'),
        ),
    ]