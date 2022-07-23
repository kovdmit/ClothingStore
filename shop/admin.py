from django.contrib import admin

from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from .models import *
from shop.models import Category


# class CustomMPTTModelAdmin(MPTTModelAdmin):
#     # отступ вложенных категорий от родительского в пикселях
#     mptt_level_indent = 20


admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Color)
# admin.site.register(Category, CustomMPTTModelAdmin)

admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)