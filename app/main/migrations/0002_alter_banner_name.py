# Generated by Django 3.2.6 on 2021-11-13 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
    ]
