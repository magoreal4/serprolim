# Generated by Django 3.2.6 on 2021-11-17 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_post_metadescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='metaDescription',
            field=models.TextField(blank=True, max_length=170),
        ),
    ]
