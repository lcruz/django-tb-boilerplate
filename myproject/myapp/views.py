from django.views.generic.base import TemplateView
from django.shortcuts import render

class MainView(TemplateView):

    def get_context_data(self, **kwargs):
		return { 'request' : self.request }