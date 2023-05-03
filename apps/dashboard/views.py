from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from apps.dashboard.forms import CategoriaForm, GaleriaForm, EntidadForm
from apps.dashboard.models import Categoria, Entidad, Galeria


class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Panel de administrador'
        context['entity'] = 'Dashboard'

        return context

    def count(self, modelo):
        c = modelo.objects.all().count()
        return c


# Categoria
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'dashboard/categoria/listado_categorias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listar Categoria'
        context['btn'] = 'Añadir Categoria'
        context['url_crear'] = reverse_lazy('categoria_create')
        context['url_listar'] = reverse_lazy('categoria_list')
        context['objects'] = Categoria.objects.all()
        return context


class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'dashboard/categoria/crear_categoria.html'
    success_url = reverse_lazy('categoria_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir Cliente'
        context['url_listar'] = self.success_url
        return context


class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'dashboard/categoria/crear_categoria.html'
    success_url = reverse_lazy('categoria_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Categoria'
        context['url_listar'] = self.success_url
        return context


class CategoriaDeleteView(DeleteView):
    model = Categoria
    success_url = reverse_lazy('categoria_list')
    template_name = 'dashboard/categoria/eliminar_categoria.html'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Categoria'
        context['url_listar'] = self.success_url
        return context


# Entidad
class EntidadListView(ListView):
    model = Entidad
    template_name = 'dashboard/entidad/listado_entidad.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listar Entidad'
        context['create_url'] = reverse_lazy('entidad_create')
        context['list_url'] = reverse_lazy('entidad_list')
        context['entity'] = 'Entidad'
        context['objects'] = Entidad.objects.all()
        return context


class EntidadCreateView(CreateView):
    model = Entidad
    form_class = EntidadForm
    template_name = 'dashboard/entidad/crear_entidad.html'
    success_url = reverse_lazy('entidad_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir Entidad'
        context['list_url'] = self.success_url
        return context


class EntidadUpdateView(UpdateView):
    model = Entidad
    form_class = EntidadForm
    template_name = 'dashboard/entidad/crear_entidad.html'
    success_url = reverse_lazy('entidad_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Entidad'
        context['list_url'] = self.success_url
        return context


class EntidadDeleteView(DeleteView):
    model = Entidad
    success_url = reverse_lazy('entidad_list')
    template_name = 'dashboard/entidad/eliminar_entidad.html'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Entidad'
        context['list_url'] = self.success_url
        return context


# Galeria
class EntidadGaleriaView(TemplateView):
    template_name = 'dashboard/entidad/galeria.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        if request.method == 'POST':
            try:
                Galeria.objects.create(entidad=Entidad.objects.get(id=kwargs['pk']), imagen=request.FILES['imagen'])
            except Exception as e:
                print(e)

        context['title'] = 'Panel de administrador | Eliminar Entidad'
        context['entity'] = 'Entidad'
        context['object_list'] = Galeria.objects.filter(entidad=kwargs['pk'])
        context['form'] = GaleriaForm
        context['entidad_id'] = kwargs['pk']

        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Panel de administrador | Eliminar Entidad'
        context['entity'] = 'Entidad'
        context['object_list'] = Galeria.objects.filter(entidad=kwargs['pk'])
        context['form'] = GaleriaForm
        context['entidad_id'] = kwargs['pk']

        return context