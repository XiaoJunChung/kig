# Generated by Django 3.2.7 on 2021-11-24 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logitem',
            name='utime',
            field=models.DateTimeField(auto_now=True, verbose_name='最後更新時間'),
        ),
    ]
