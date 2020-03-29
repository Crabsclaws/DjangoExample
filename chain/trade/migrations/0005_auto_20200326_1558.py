# Generated by Django 3.0.2 on 2020-03-26 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0004_auto_20200326_1517'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buy',
            options={'ordering': ['date'], 'verbose_name': '交易表', 'verbose_name_plural': '交易表'},
        ),
        migrations.AlterModelOptions(
            name='sell',
            options={'verbose_name': '交易表', 'verbose_name_plural': '交易表'},
        ),
        migrations.AlterField(
            model_name='buy',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='buy',
            name='serial_no',
            field=models.CharField(default='20200326155849-2-1585209529', max_length=50),
        ),
        migrations.AlterField(
            model_name='sell',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='sell',
            name='serial_no',
            field=models.CharField(default='20200326155849-1-1585209529', max_length=50),
        ),
    ]
