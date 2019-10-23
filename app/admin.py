from django.contrib import admin
from .models import Photo, Category, Relationship

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


# django adminに出すリスト ID TITLE
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class RelationshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'follow', 'follower')
    list_display_links = ('id', 'follow', 'follower')


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Relationship, RelationshipAdmin)
