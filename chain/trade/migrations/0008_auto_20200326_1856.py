# Generated by Django 3.0.2 on 2020-03-26 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0007_auto_20200326_1726'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buy',
            options={'ordering': ['date'], 'verbose_name': '收购表', 'verbose_name_plural': '收购表'},
        ),
        migrations.AlterModelOptions(
            name='sell',
            options={'verbose_name': '出售表', 'verbose_name_plural': '出售表'},
        ),
        migrations.AlterField(
            model_name='buy',
            name='serial_no',
            field=models.CharField(default='20200326185621-2-1585220181', max_length=50),
        ),
        migrations.AlterField(
            model_name='buyrecord',
            name='serial_no',
            field=models.CharField(default='20200326185621-4-1585220181', max_length=50),
        ),
        migrations.AlterField(
            model_name='sell',
            name='serial_no',
            field=models.CharField(default='20200326185621-1-1585220181', max_length=50),
        ),
        migrations.AlterField(
            model_name='sellrecord',
            name='serial_no',
            field=models.CharField(default='20200326185621-3-1585220181', max_length=50),
        ),
    ]
