# Generated by Django 4.0.5 on 2022-08-09 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_rename_dateofbirth_post_dateshare'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='forename',
        ),
        migrations.RemoveField(
            model_name='post',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='post',
            name='year',
        ),
        migrations.AddField(
            model_name='post',
            name='textinfo',
            field=models.TextField(max_length=500, null=True, verbose_name='Text info'),
        ),
        migrations.AddField(
            model_name='post',
            name='textpost',
            field=models.TextField(null=True, verbose_name='Text post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='dateshare',
            field=models.DateField(blank=True, null=True, verbose_name='Share Date'),
        ),
    ]
