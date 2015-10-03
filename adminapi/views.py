# -*- coding: utf-8 -*-

import adminapi

from django.http import HttpResponse
from django.views.generic import View

class IndexView(View):

    def get(self, request):
        return HttpResponse("{0} - {1}".format(
            adminapi.__name__, adminapi.__version__))
