# Generated by Django 4.0.4 on 2022-04-25 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justSaid_web', '0003_post_title_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(max_length=255),
        ),
    ]