from django.contrib import admin
from .models import*

@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display=[
        "icon_image",
    "icon_name",

    ]


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display=[
        "project_name",
        "thumbnail",
        "live_link",
        "uses_tools",
    ]


@admin.register(MySkill)
class MyskillAdmin(admin.ModelAdmin):
    list_display=[
        "teck_name",
        "perchange",
        "description",
        "image",
    ]