from django.contrib import admin
from . import models

@admin.register(models.Board)
class BoardAdmin(admin.ModelAdmin):
    fieldsets = (
        ("기본정보", {
            "fields": ("title","content","tag","writer",),
        }),
    )
    
    list_display = ("title","writer","Tag","created_at")
    search_fields = ("title","Tag")
    
    def Tag(self,obj):
        tags = obj.tag.all()
        tag_list = []
        for t in tags:
            tag_list.append(t)
        return tag_list if len(tag_list) < 5 else tag_list[:5]
    Tag.short_description = "태그"
    
    
@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    fieldsets = (
        ("기본정보", {
            "fields": (
                "name",
            ),
        }),
    )
    list_display = ("name",)
    