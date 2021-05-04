# Generated by Django 3.1.4 on 2021-04-30 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0007_auto_20210430_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='cfolder',
        ),
        migrations.AddField(
            model_name='folder',
            name='parent_folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cloud.folder'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='partition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cloud.userpartition'),
        ),
        migrations.DeleteModel(
            name='cFolder',
        ),
    ]