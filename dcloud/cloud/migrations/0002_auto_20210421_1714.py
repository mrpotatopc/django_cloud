# Generated by Django 3.1.4 on 2021-04-21 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='Folder',
            new_name='folder',
        ),
        migrations.RenameField(
            model_name='userpartition',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='userpartition',
            old_name='User',
            new_name='user',
        ),
    ]
