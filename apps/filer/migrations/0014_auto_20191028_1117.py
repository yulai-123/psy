# Generated by Django 2.2.5 on 2019-10-28 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0013_auto_20191015_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='fakemodel',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='关联文件名'),
        ),
        migrations.AddField(
            model_name='fakemodel',
            name='relate_id',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='关联文件夹id'),
        ),
    ]