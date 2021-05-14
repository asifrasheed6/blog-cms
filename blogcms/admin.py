from django.contrib import admin
from blogcms.models import Category, Post, Comment, View, Embed, Image, UserImage

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(View)
admin.site.register(Embed)
admin.site.register(Image)
admin.site.register(UserImage)
