# Generated by Django 2.2.1 on 2019-09-29 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Saller', '0003_vaild_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaild_code',
            name='code_time',
            field=models.FloatField(verbose_name='创建时间'),
        ),
    ]