# Generated by Django 3.0.2 on 2020-03-26 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0004_coinrule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
