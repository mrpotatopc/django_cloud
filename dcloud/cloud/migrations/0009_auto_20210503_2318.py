# Generated by Django 3.1.4 on 2021-05-03 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0008_auto_20210501_0202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cfolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pfolder1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cloud.folder')),
                ('pfolder2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cloud.cfolder')),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='folder2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cloud.cfolder'),
        ),
    ]
