# -*- coding: utf-8 -*-

import adminapi

from django.http import JsonResponse
from django.contrib.admin.sites import site as admin_site
from django.views.generic import View

class IndexView(View):

    def sanitize_response(self, json):
        """Remove attributes from the response that can't be json serialized"""

        json.pop("site_header")
        json.pop("site_title")
        json.pop("title")
        for app in json.get("app_list"):
            app.pop("name")
            for model in app.get("models"):
                model.pop("name")
        return json

    def get(self, request):
        html = admin_site.index(request)
        return JsonResponse(self.sanitize_response(html.context_data))
