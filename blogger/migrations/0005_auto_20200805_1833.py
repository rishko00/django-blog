# Generated by Django 3.0.7 on 2020-08-05 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0004_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.IntegerField(),
        ),
    ]