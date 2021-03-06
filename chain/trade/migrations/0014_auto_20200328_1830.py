# Generated by Django 3.0.2 on 2020-03-28 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0013_auto_20200328_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='serial_no',
            field=models.CharField(default='20200328183033-2-1585391433', max_length=50),
        ),
        migrations.AlterField(
            model_name='buy',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, '可预定'), (1, '待付款'), (2, '取消'), (3, '完成'), (4, '删除')], default=0, help_text='状态', verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='buyrecord',
            name='serial_no',
            field=models.CharField(default='20200328183033-4-1585391433', max_length=50),
        ),
        migrations.AlterField(
            model_name='buyrecord',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, '待支付'), (1, '已支付'), (2, '取消'), (3, '已完成')], default=0, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='record',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, '可预定'), (1, '待付款'), (2, '取消'), (3, '完成'), (4, '删除')], default=1, help_text='状态', verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='sell',
            name='serial_no',
            field=models.CharField(default='20200328183033-1-1585391433', max_length=50),
        ),
        migrations.AlterField(
            model_name='sell',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, '可预定'), (1, '待付款'), (2, '取消'), (3, '完成'), (4, '删除')], default=0, help_text='状态', verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='sellrecord',
            name='serial_no',
            field=models.CharField(default='20200328183033-3-1585391433', max_length=50),
        ),
        migrations.AlterField(
            model_name='trade',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, '可预定'), (1, '待付款'), (2, '取消'), (3, '完成'), (4, '删除')], default=0, help_text='状态', verbose_name='状态'),
        ),
    ]
