# Generated by Django 4.0.5 on 2022-08-09 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_alter_post_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='medianame',
            field=models.CharField(max_length=100, null=True, verbose_name='media name'),
        ),
    ]
