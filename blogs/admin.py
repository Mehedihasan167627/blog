from django.contrib import admin

# Register your models here.
from .models import*

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=["title",
        "tag_list",
        "view_count",
        "is_popular",
        "status",
         "is_hero",
        ]
    list_editable=("view_count","status","is_popular","is_hero")
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=[
        "name",
        "show_case_type",
        "ordering",
        "home_page_items",
        "ordering",
        "status",
        "slug",
        ]
    list_editable=[
        "show_case_type",
        "ordering",
       "home_page_items",
        "status",
    ]
    exclude=("slug",)
    

admin.site.register([Comment,ReplyComment])