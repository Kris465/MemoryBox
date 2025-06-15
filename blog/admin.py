
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'pub_date')
    list_filter = ('category', 'pub_date')
    search_fields = ('title', 'content')
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
