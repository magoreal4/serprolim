# Generated by Django 3.2.6 on 2021-11-17 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_anuncio_display'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
