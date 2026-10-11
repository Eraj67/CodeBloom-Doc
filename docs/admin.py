from django.contrib import admin
from .models import Document, Category

# Register your models here.
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'syntax', 
        'key', 
        'example', 
        'mistake', 
        'summary'
        )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)    