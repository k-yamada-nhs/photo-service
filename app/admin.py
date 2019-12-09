from django.contrib import admin
from .models import Photo, Relationship, Comnt, Reply, Like

# Register your models here.

# django adminに出すリスト ID TITLE
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class RelationshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'follow', 'follower')
    list_display_links = ('id', 'follow', 'follower')

class ComntAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')

class ReplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')

class LikeAdmin(admin.ModelAdmin):
    list_display = ['id',]
    list_display_links = ['id',]


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Relationship, RelationshipAdmin)
admin.site.register(Comnt, ComntAdmin)
admin.site.register(Reply, ReplyAdmin)
admin.site.register(Like, LikeAdmin)
