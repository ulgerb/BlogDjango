# Generated by Django 4.0.5 on 2022-08-11 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0017_rename_created_date_comments_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='user',
            new_name='post',
        ),
    ]