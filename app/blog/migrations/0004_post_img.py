# Generated by Django 3.2.6 on 2021-11-12 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211112_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
