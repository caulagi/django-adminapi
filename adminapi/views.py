# -*- coding: utf-8 -*-

from django.apps import apps
from django.contrib.admin.sites import site as admin_site
from django.http import JsonResponse
from django.views.generic import View

from .serializers import FieldSerializer

class IndexView(View):

    def _sanitize_response(self, request, json):
        """Remove attributes from the response that can't be json serialized"""

        json.pop("site_header")
        json.pop("site_title")
        json.pop("title")
        for app in json.get("app_list"):
            app.pop("name")
            for model in app.get("models"):
                model.pop("name")
                db_model = apps.get_model(app_label=app.get("app_label"),
                    model_name=model.get("object_name"))
                for (registry_model, admin_model) in admin_site._registry.iteritems():
                    if registry_model._meta.db_table == db_model._meta.db_table:
                        model["fields"] = []
                        for field in admin_model.get_form(request).base_fields.itervalues():
                            model["fields"].append(FieldSerializer(field).to_dict())
        return json

    def get(self, request):
        html = admin_site.index(request)
        return JsonResponse(self._sanitize_response(request, html.context_data))
