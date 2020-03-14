# Generated by Django 3.0.2 on 2020-03-10 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='展示的标题', max_length=30, unique=True, verbose_name='标题')),
                ('calculate', models.FloatField(help_text='矿机的计算能力', verbose_name='计算能力')),
                ('rent', models.IntegerField(help_text='租金', verbose_name='租金')),
                ('output', models.FloatField(help_text='产出总量', verbose_name='产出总量')),
                ('limit', models.IntegerField(help_text='限制租赁的数量', verbose_name='限制租赁数量')),
                ('number', models.IntegerField(help_text='当前可以租赁的数量', verbose_name='当前剩余数量')),
            ],
            options={
                'verbose_name': '矿机数据库',
                'verbose_name_plural': '矿机数据库',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='标题', max_length=60, verbose_name='标题')),
                ('img', models.CharField(blank=True, default='', help_text='图片', max_length=256, verbose_name='图片')),
                ('url', models.CharField(blank=True, default='', help_text='文章链接', max_length=256, verbose_name='文章链接')),
            ],
            options={
                'verbose_name': '新闻表',
                'verbose_name_plural': '新闻表',
            },
        ),
        migrations.CreateModel(
            name='Trading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin', models.FloatField(help_text='币的数量', verbose_name='币数量')),
                ('datetime', models.DateTimeField(auto_now=True, help_text='发布时间日期', verbose_name='发布日期')),
                ('status', models.SmallIntegerField(choices=[('进行中', 1), ('结束', 2)], default=1, help_text='交易状态', verbose_name='交易状态')),
                ('type', models.SmallIntegerField(choices=[('出售', 1), ('收购', 2)], default=1, help_text='交易类型', verbose_name='交易类型')),
                ('user', models.ForeignKey(help_text='用户ID', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '出售/收购列表',
                'verbose_name_plural': '出售/收购列表',
            },
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField(help_text='出售的分数', verbose_name='分数')),
                ('datetime', models.DateTimeField(auto_now=True, help_text='日期时间', verbose_name='日期时间')),
                ('buyer', models.ForeignKey(help_text='收购者的ID', on_delete=django.db.models.deletion.CASCADE, related_name='收购者', to=settings.AUTH_USER_MODEL, verbose_name='收购者')),
                ('seller', models.ForeignKey(help_text='出售者的ID', on_delete=django.db.models.deletion.CASCADE, related_name='出售者', to=settings.AUTH_USER_MODEL, verbose_name='出售者')),
            ],
            options={
                'verbose_name': '交易记录',
                'verbose_name_plural': '交易记录',
            },
        ),
        migrations.CreateModel(
            name='NewsRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True, help_text='记录的时间', verbose_name='时间')),
                ('news', models.ForeignKey(help_text='新闻id', on_delete=django.db.models.deletion.CASCADE, related_name='news', to='chains.News', verbose_name='新闻')),
                ('user', models.ForeignKey(help_text='用户id', on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='用户信息')),
            ],
            options={
                'verbose_name': '新闻观看记录',
                'verbose_name_plural': '新闻观看记录',
            },
        ),
        migrations.CreateModel(
            name='MachineRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine', models.ForeignKey(help_text='对应矿机的外键', on_delete=django.db.models.deletion.CASCADE, to='chains.Machine', verbose_name='对应矿机的外键')),
                ('user', models.ForeignKey(help_text='租赁用户的ID', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='租赁的用户')),
            ],
            options={
                'verbose_name': '矿机出售列表',
                'verbose_name_plural': '矿机出售列表',
            },
        ),
    ]