# Generated by Django 2.2.1 on 2019-10-15 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0009_useradress'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='status',
            field=models.IntegerField(choices=[(0, '未支付'), (1, '已支付'), (2, '已发货'), (3, '已完成')], default=0),
        ),
    ]
