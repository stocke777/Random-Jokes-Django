# Generated by Django 2.2.5 on 2020-02-08 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joke', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jokelist',
            name='content',
            field=models.TextField(default='hola'),
            preserve_default=False,
        ),
    ]