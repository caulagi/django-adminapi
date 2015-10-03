# -*- coding: utf-8 -*-


from django.conf.urls import patterns, include, url
from django.contrib import admin
from adminapi.sites import site as adminapi_site

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/admin/', include(adminapi_site.urls)),
)
