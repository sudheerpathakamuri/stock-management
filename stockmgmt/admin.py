from django.contrib import admin
from .forms import StockCreateForm
from .models import *

# Register your models here.
class StockCreateAdmin(admin.ModelAdmin):
	list_display = ['category','item_name','quantity','date']
	form = StockCreateForm
	list_filter = ['category']
	search_fields = ['category','item_name']

admin.site.register(Stock,StockCreateAdmin)
admin.site.register(category)
