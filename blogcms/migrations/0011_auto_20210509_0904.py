# Generated by Django 3.0 on 2021-05-09 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogcms', '0010_auto_20210509_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=17),
        ),
    ]