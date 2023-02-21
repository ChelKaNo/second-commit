from django.contrib import admin

from .models import Product, Bin, Home

#admin.site.register(Product)
admin.site.register(Bin)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'cost']
    list_filter = ['cost']
    search_fields = ['title']

@admin.register(Home)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['size', 'cost', 'adr', 'bal']