from django.contrib import admin
from .models import Blog,Category,Comment
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    list_display = ['name', 'slug']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog)
admin.site.register(Comment)