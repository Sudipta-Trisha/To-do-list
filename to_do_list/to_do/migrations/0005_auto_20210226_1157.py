# Generated by Django 3.1.6 on 2021-02-26 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0004_list_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='title',
            new_name='details',
        ),
    ]
