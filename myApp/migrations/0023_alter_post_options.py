# Generated by Django 4.0.5 on 2022-08-11 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0022_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['id']},
        ),
    ]
