from django.contrib import admin

from .models import Product, Category, Size, Color


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Size)
admin.site.register(Color)