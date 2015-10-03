# -*- coding: utf-8 -*-

import views

from django.conf.urls import url


class AdminApiSite(object):

    def __init__(self, name="adminapi"):
        self.name = name
        
    def get_urls(self):
        return [
           url(r'^$', views.IndexView.as_view(), name="adminapi-index"),
        ]

    @property
    def urls(self):
        return self.get_urls(), "adminapi", self.name

site = AdminApiSite()
