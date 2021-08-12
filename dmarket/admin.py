from django.contrib import admin
from .models import Tovar_market,Vremy_market

@admin.register(Tovar_market)
class Tovar_marketAdmin(admin.ModelAdmin):
	list_display =('name','kolfek','kol','payself','paymin','pay_max','pamax','pasred','Steam_price','zatype','account')
	list_filter = ('account','zatype','name','pay_max')
	list_per_page = 25
	search_fields = ['name']
# Register your models here.
@admin.register(Vremy_market)
class Vremy_marketAdmin(admin.ModelAdmin):
	list_display =('time',)
