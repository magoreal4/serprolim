# Generated by Django 3.2.6 on 2021-11-16 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20211116_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='display',
            field=models.BooleanField(default=False),
        ),
    ]