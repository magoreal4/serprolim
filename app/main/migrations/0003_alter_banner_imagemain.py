# Generated by Django 3.2.6 on 2021-11-15 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_banner_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='imagemain',
            field=models.ImageField(null=True, upload_to='imagemain', verbose_name='imagenmain'),
        ),
    ]