from django.contrib import admin
from django.template.defaultfilters import title

from .models import News, Category, Contact

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', "slug", "publish_time", "status"]
    list_filter = ['status', 'created_time', "publish_time"]
    prepopulated_fields = {"slug": ('title',)}
    data_hierarchy = 'publish_time'
    search_fields = ['title', 'body']
    ordering = ['status', 'publish_time']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', "name"]
    # search_fields = ['name', 'body']


admin.site.register(Contact)


# Register your models here.
