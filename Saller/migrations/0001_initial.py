# Generated by Django 2.2.1 on 2019-09-24 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_label', models.CharField(max_length=32)),
                ('type_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=32)),
                ('username', models.CharField(blank=True, max_length=32, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='img')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=4, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('user_type', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_number', models.CharField(max_length=11, verbose_name='商品编号')),
                ('goods_name', models.CharField(max_length=32, verbose_name='商品名称')),
                ('goods_price', models.FloatField(verbose_name='价格')),
                ('goods_count', models.IntegerField(verbose_name='数量')),
                ('goods_location', models.CharField(max_length=254, verbose_name='产地')),
                ('goods_safe_date', models.IntegerField(verbose_name='保质期')),
                ('goods_status', models.IntegerField(default=1, verbose_name='状态')),
                ('goods_pro_time', models.DateField(auto_now=True, verbose_name='生产日期')),
                ('picture', models.ImageField(upload_to='img')),
                ('goods_store', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Saller.LoginUser')),
                ('goods_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Saller.GoodsType')),
            ],
        ),
    ]
