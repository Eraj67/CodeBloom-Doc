from django.contrib import admin
from .models import Document, Category, Example

# Register your models here.
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'syntax', 
        'key', 
        'mistake', 
        'summary'
        )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)    

@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ('__str__','document', 'language')