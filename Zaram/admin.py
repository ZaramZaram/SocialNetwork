from django.contrib import admin
from Zaram.models import Post,PostLike, PostImage

class PostLikeInLine(admin.TabularInline):
    model = PostLike

class PostImageInLine(admin.TabularInline):
    model = PostImage

class PostAdmin(admin.ModelAdmin) :
    inlines = [PostLikeInLine, PostImageInLine]

admin.site.register(Post, PostAdmin)