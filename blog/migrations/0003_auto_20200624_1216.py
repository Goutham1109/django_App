# Generated by Django 2.2.11 on 2020-06-24 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200624_1207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='Title',
            new_name='blogtitle',
        ),
    ]
