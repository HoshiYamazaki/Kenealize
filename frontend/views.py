# Create your views here.
import datetime

from django.views.generic import TemplateView
from django_common.mixin import LoginRequiredMixin

from collect.models import Execution
from kencan import KenCan


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """Get context data."""
        context = super().get_context_data(**kwargs)
        KenCanAPI = KenCan()
        data = KenCanAPI.get_db_data()
        data['from_index'] = True
        Execution.objects.create(**data)
        context['scan_data'] = KenCanAPI.get_lan_hosts()
        context['exec_time'] = KenCanAPI.get_search_exec_time()
        context['host_amount'] = KenCanAPI.get_hosts_amount()
        context['nmap_ver'] = KenCanAPI.get_nmap_version()
        return context
