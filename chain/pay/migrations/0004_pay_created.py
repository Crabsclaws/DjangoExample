# Generated by Django 3.0.2 on 2020-03-29 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0003_pay_use'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='创建日期', null=True, verbose_name='created_time'),
        ),
    ]
