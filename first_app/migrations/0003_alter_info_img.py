# Generated by Django 3.2.5 on 2021-07-28 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='img',
            field=models.URLField(),
        ),
    ]
