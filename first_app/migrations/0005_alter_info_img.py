# Generated by Django 3.2.5 on 2021-07-28 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_alter_info_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='img',
            field=models.ImageField(upload_to='images'),
        ),
    ]
