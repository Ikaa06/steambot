# Generated by Django 2.2.4 on 2020-04-10 13:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dmarket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tovar_market',
            name='Steam_price',
            field=models.CharField(default=django.utils.timezone.now, help_text='5.25', max_length=30, verbose_name='Рекомендуемая цена в Steam:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tovar_market',
            name='kol',
            field=models.CharField(default=django.utils.timezone.now, help_text='2', max_length=30, verbose_name='Максимальное увеличение$'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tovar_market',
            name='kolfek',
            field=models.CharField(default=django.utils.timezone.now, help_text='0.01', max_length=30, verbose_name='Увелечение ставки$'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tovar_market',
            name='pasred',
            field=models.CharField(help_text='5.25', max_length=30, verbose_name='Средняя рыночная цена:'),
        ),
    ]
