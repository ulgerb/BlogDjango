# Generated by Django 4.0.5 on 2022-08-12 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0028_alter_post_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Current',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ManyToManyField(blank=True, null=True, to='myApp.post')),
            ],
        ),
    ]