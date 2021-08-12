# Generated by Django 2.2.4 on 2020-04-04 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tovar_market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Название товара')),
                ('payself', models.CharField(help_text='0.25', max_length=30, verbose_name='Вы заплатите$')),
                ('pay_max', models.CharField(help_text='1.25', max_length=30, verbose_name='Максимальная цена заказа на рынке:')),
                ('pamax', models.CharField(help_text='1.25', max_length=30, verbose_name='Минимальная рыночная цена:')),
                ('pasred', models.CharField(help_text='5.25', max_length=30, verbose_name='Рекомендуемая цена в Steam:')),
                ('zatype', models.CharField(blank=True, choices=[('1', 'Неактивный'), ('0', 'Активный')], max_length=200, verbose_name='Состояние')),
                ('account', models.CharField(max_length=30, verbose_name='Аккаунт')),
            ],
            options={
                'verbose_name': 'Заказ придмета',
                'verbose_name_plural': 'Заказы придметов',
                'db_table': 'Tovar_market',
            },
        ),
    ]
