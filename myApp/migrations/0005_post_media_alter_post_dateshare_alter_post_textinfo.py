# Generated by Django 4.0.5 on 2022-08-09 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_remove_post_forename_remove_post_surname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Blog Resmi'),
        ),
        migrations.AlterField(
            model_name='post',
            name='dateshare',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Share Date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='textinfo',
            field=models.TextField(max_length=1000, null=True, verbose_name='Text info'),
        ),
    ]
