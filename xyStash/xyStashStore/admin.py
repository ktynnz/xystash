from django.contrib import admin

# Register your models here.

#detail and tell django what models we want to access in the admin area
#describe what it is we want to include
from .models import Category, Product, user, fromContactForm
# from .models import subscriber

admin.site.register(user)
# admin.site.register(subscriber)

@admin.register(fromContactForm)
class fromContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'created']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description', 'price', 'in_stock', 
        'is_active', 'created', 'updated' ]
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}