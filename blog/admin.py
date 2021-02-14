from django.contrib import admin
from blog.models import category, article, comment


# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )
    list_display = (
        'name',
    )


admin.site.register(category, categoryAdmin)


class articlesAdmin(admin.ModelAdmin):
    search_fields = (
        'header', 'content',
    )
    list_display = (
        'header', 'content', 'existed_date', 'edited_date',
    )


admin.site.register(article, articlesAdmin)


class commentAdmin(admin.ModelAdmin):
    search_fields = (
        'author','article','comment',
    )
    list_display = (
        'author','article','comment',
    )


admin.site.register(comment, commentAdmin)
