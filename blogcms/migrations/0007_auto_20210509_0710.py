# Generated by Django 3.0 on 2021-05-09 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogcms', '0006_view_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='view',
            name='cover',
        ),
        migrations.AddField(
            model_name='postdata',
            name='cover',
            field=models.BooleanField(default=False),
        ),
    ]
