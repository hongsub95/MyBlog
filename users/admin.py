from atexit import register
from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        ("기본정보", {
            'fields': ("username","name","gender",),
        }),
        ("부가정보",{"fields":("phone_number","birthday")}),
        ("기타",{"fields":("superhost",)})
    )
    list_display = (
        "username",
        "birthday",
        "phone_number",
    )
