# Generated by Django 3.0 on 2021-05-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogcms', '0016_post_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
