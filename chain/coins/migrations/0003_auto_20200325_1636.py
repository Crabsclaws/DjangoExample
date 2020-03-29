# Generated by Django 3.0.2 on 2020-03-25 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0002_auto_20200323_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='key',
            field=models.CharField(choices=[('sign', '注册'), ('news', '阅读新闻'), ('machine', '机器'), ('trade', '交易'), ('post_advert', '发布广告')], help_text='奖励的key 根据key进行搜索是否有存在', max_length=50, unique=True, verbose_name='奖励的key'),
        ),
    ]