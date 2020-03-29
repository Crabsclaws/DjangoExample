# Generated by Django 3.0.2 on 2020-03-26 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trade', '0002_auto_20200323_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.FloatField(verbose_name='交易的数量总量')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '默认状态'), (1, '待付款'), (2, '取消'), (3, '完成'), (4, '删除')], default=0, help_text='状态', verbose_name='状态')),
                ('serial_no', models.CharField(default='20200326141512-2-1585203312', max_length=50)),
                ('user', models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '交易表',
                'verbose_name_plural': '交易表',
            },
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.FloatField(verbose_name='交易的数量总量')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '默认状态'), (1, '待付款'), (2, '取消'), (3, '完成'), (4, '删除')], default=0, help_text='状态', verbose_name='状态')),
                ('serial_no', models.CharField(default='20200326141512-1-1585203312', max_length=50)),
                ('user', models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '交易表',
                'verbose_name_plural': '交易表',
            },
        ),
        migrations.CreateModel(
            name='SellRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '待付款'), (1, '已付款'), (2, '取消'), (3, '已完成')], verbose_name='状态')),
                ('sell', models.ForeignKey(help_text='相关订单', on_delete=django.db.models.deletion.CASCADE, related_name='sell', to='trade.Sell', verbose_name='sell')),
                ('user', models.ForeignKey(help_text='出售者', on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL, verbose_name='提交者')),
            ],
            options={
                'verbose_name': '出售记录',
                'verbose_name_plural': '出售记录',
            },
        ),
        migrations.CreateModel(
            name='BuyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '待支付'), (1, '已支付'), (2, '取消'), (3, '已完成')], verbose_name='状态')),
                ('buy', models.ForeignKey(help_text='相关订单', on_delete=django.db.models.deletion.CASCADE, related_name='buy', to='trade.Buy', verbose_name='buy')),
                ('user', models.ForeignKey(help_text='出售者', on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL, verbose_name='提交者')),
            ],
            options={
                'verbose_name': '出售记录',
                'verbose_name_plural': '出售记录',
            },
        ),
    ]
