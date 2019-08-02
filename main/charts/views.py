"""charts view
"""
from django.shortcuts import render
from django.views import View

from helpers.charts import Charts

class ChartsView(View):

    def __init__(self):
        self.api = Charts()

    def get(self, request):
        """
        :param request:
        :return:
        """
        template, result = self.api.get_charts(request=request)
        return render(request, template, result)