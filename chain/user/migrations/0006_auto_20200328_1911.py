# Generated by Django 3.0.2 on 2020-03-28 19:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200328_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinuserinfo',
            name='address',
            field=models.CharField(default=uuid.UUID('57de6cac-7ef8-52f6-abfe-862b2a40e21f'), help_text='地址', max_length=100, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='identifier',
            name='number',
            field=models.CharField(help_text='用户身份证信息', max_length=20, verbose_name='ID'),
        ),
    ]
