# Generated by Django 4.0.5 on 2022-08-12 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0031_remove_current_post_current_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Current',
            new_name='CurrentPost',
        ),
    ]
