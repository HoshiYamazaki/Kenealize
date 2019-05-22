# Create your views here.
from django.views.generic import TemplateView

from kencan import KenCan


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """Get context data."""
        context = super().get_context_data(**kwargs)
        KenCanAPI = KenCan()
        context['scan_data'] = KenCanAPI.get_lan_hosts()
        context['exec_time'] = KenCanAPI.get_search_exec_time()
        context['host_amount'] = KenCanAPI.get_hosts_amount()
        context['nmap_ver'] = KenCanAPI.get_nmap_version()
        return context
