from django.db import models


class Tovar_market(models.Model):
    # chat_id = models.PositiveIntegerField(verbose_name='ID модератора',unique=True,blank=True,null=True)
    name = models.CharField(verbose_name='Название товара', max_length=200, blank=True)
    kolfek = models.CharField(verbose_name='Увелечение ставки$', max_length=30, help_text='0.01')
    kol = models.CharField(verbose_name='Порог$', max_length=30, help_text='2')
    # kol = models.CharField(verbose_name='Максимальное увеличение$',max_length=30,help_text='2')
    paymin = models.CharField(verbose_name='Минимальная цена снижения', max_length=30, help_text='45')
    payself = models.CharField(verbose_name='Вы заплатите$', max_length=30, help_text='0.25')
    pay_max = models.CharField(verbose_name='Максимальная цена заказа на рынке:', max_length=30, help_text='1.25')
    pamax = models.CharField(verbose_name='Минимальная рыночная цена:', max_length=30, help_text='1.25')
    pasred = models.CharField(verbose_name='Средняя рыночная цена:', max_length=30, help_text='5.25')
    Steam_price = models.CharField(verbose_name='Рекомендуемая цена в Steam:', max_length=30, help_text='5.25')
    SOSTOYNUE = [('1', 'Неактивный'), ('0', 'Активный')]
    zatype = models.CharField(max_length=200, choices=SOSTOYNUE, blank=True, verbose_name='Состояние')
    account = models.CharField(verbose_name='Аккаунт', max_length=30)

    # SOSTOE = [('0', 'В работе'),('1', 'Не работает')]
    # zaty = models.CharField(max_length=200,choices=SOSTOE,blank=True,verbose_name='Имент копию')
    # birhday = models.DateField(verbose_name='Дата',help_text='25.11.2000')

    def __str__(self):
        return f'Товар|{self.name}'

    class Meta:
        db_table = 'Tovar_market'
        verbose_name = 'Заказ придмета'
        verbose_name_plural = 'Заказы придметов'


class Vremy_market(models.Model):
    time = models.CharField(verbose_name='Ведите время в минутах', max_length=200)

    class Meta:
        db_table = 'Vremy_market'
        verbose_name = 'Время повторения запроса'
        verbose_name_plural = 'Время повторения запроса'
