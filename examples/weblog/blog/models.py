# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    TITLE_MAX_LENGTH = 100

    title = models.CharField(max_length=TITLE_MAX_LENGTH, unique=True)
    slug = models.SlugField(max_length=TITLE_MAX_LENGTH, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag, null=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.content[:20]
