# Generated by Django 4.0.5 on 2022-08-09 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_post_media_alter_post_dateshare_alter_post_textinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name2',
            field=models.CharField(max_length=50, null=True, verbose_name='Post name'),
        ),
    ]
