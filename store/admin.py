from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

class ProductAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

class CategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)
