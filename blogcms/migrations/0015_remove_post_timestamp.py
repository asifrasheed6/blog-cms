# Generated by Django 3.0 on 2021-05-09 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogcms', '0014_auto_20210509_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='timestamp',
        ),
    ]