from django.contrib import admin

# Register your models here.
from BlogApp.models import Post,Comment
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','publish','created','updated','status']
    list_filter = ('status','created','publish','author')
    search_fields = ('title','body')
    prepopulated_fields = {"slug":('title',)}
    raw_id_fields = ('author',)
    ordering = ['status','publish']

admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','post','body','created','updated','active']
    list_filter = ['created','updated','active']
    search_fields = ['name','email','body']

admin.site.register(Comment,CommentAdmin)