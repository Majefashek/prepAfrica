from django.views.generic.base import TemplateView
from django.shortcuts import render


class DashBoardView(TemplateView):
    template_name = "core_app/dashboard.html"
