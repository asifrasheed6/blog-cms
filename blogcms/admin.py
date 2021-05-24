from django.contrib import admin
from blogcms.models import Category, Post, Comment, View, Image, UserImage

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(View)
admin.site.register(Image)
admin.site.register(UserImage)
