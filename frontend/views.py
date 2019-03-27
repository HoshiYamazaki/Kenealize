# Create your views here.
from django.views.generic import TemplateView

from kencan import KenCan


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """Get context data."""
        context = super().get_context_data(**kwargs)
        KenCanAPI = KenCan()
        print(KenCanAPI.scan_device('192.168.1.48'))
        return context
