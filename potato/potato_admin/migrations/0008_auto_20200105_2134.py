# Generated by Django 3.0.1 on 2020-01-05 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potato_admin', '0007_auto_20200104_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True, help_text='最新的更新日期', verbose_name='最新更新日期')),
                ('create', models.DateTimeField(auto_now_add=True, help_text='创建日期', verbose_name='创建日期')),
                ('name', models.CharField(help_text='唯一的用户名 不可以重复', max_length=128, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='num',
            field=models.CharField(default='2020-01-05 21:34:10', help_text='订单号，如果没有订单号的时候会默认设置成日期', max_length=100, verbose_name='订单号'),
        ),
    ]
