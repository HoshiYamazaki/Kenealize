from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from kencan import KenCan


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """Get context data."""
        context = super().get_context_data(**kwargs)
        KenCanAPI = KenCan()
        context['nmap'] = KenCanAPI.scan_network()
        context['data'] = KenCanAPI.devices_ips
        return context