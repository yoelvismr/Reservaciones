from django.views.generic import TemplateView, CreateView, ListView

from django.urls import reverse_lazy

from apps.dashboard.models import *

from .forms import *
from .models import *


class Index(TemplateView):
    template_name = 'inicio/index.html'


class ReservacionGastronmicaView(ListView):
    model = ReservacionGastronmica
    template_name = 'reservaciones/gastronomia/listado_reservaciones.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reservaciones'
        context['create_url'] = reverse_lazy('crear_reservacion_gastronomica')
        context['list_url'] = reverse_lazy('listado_reservaciones_gastronomicas')
        context['entity'] = 'Entidad'
        context['object_list'] = Entidad.objects.all()
        return context


class ReservacionGastronmicaCreateView(CreateView):
    model = ReservacionGastronmica
    form_class = ReservacionGastronmicaForm
    template_name = 'dashboard/entidad/crear_entidad.html'
    success_url = reverse_lazy('reservaciones_gastronomicas')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir Reservación'
        context['list_url'] = self.success_url
        return context
