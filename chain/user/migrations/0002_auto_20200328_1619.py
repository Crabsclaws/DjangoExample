# Generated by Django 3.0.2 on 2020-03-28 16:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinuserinfo',
            name='address',
            field=models.CharField(default=uuid.UUID('d3fb8daa-830e-5817-86f9-16de5ec84e43'), help_text='地址', max_length=100, verbose_name='地址'),
        ),
    ]