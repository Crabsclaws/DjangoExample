# Generated by Django 3.0.2 on 2020-03-28 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0015_auto_20200328_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='serial_no',
            field=models.CharField(default='20200328191103-2-1585393863', max_length=50),
        ),
        migrations.AlterField(
            model_name='buyrecord',
            name='serial_no',
            field=models.CharField(default='20200328191103-4-1585393863', max_length=50),
        ),
        migrations.AlterField(
            model_name='sell',
            name='serial_no',
            field=models.CharField(default='20200328191103-1-1585393863', max_length=50),
        ),
        migrations.AlterField(
            model_name='sellrecord',
            name='serial_no',
            field=models.CharField(default='20200328191103-3-1585393863', max_length=50),
        ),
    ]
