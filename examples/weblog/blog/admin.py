# -*- coding: utf-8 -*-

from django.contrib import admin
from blog.models import Tag, Post


class TagAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
