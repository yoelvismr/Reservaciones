from django.urls import path

from apps.dashboard.views import *

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    # Categoria
    path('categoria/list/', EntidadListView.as_view(), name='categoria_list'),
    path('categoria/create/', EntidadCreateView.as_view(), name='categoria_create'),
    path('categoria/update/<int:pk>', EntidadUpdateView.as_view(), name='categoria_update'),
    path('categoria/delete/<int:pk>', EntidadDeleteView.as_view(), name='categoria_delete'),
    # Entidad
    path('entidad/list/', EntidadListView.as_view(), name='entidad_list'),
    path('entidad/create/', EntidadCreateView.as_view(), name='entidad_create'),
    path('entidad/update/<int:pk>', EntidadUpdateView.as_view(), name='entidad_update'),
    path('entidad/delete/<int:pk>', EntidadDeleteView.as_view(), name='entidad_delete'),
    # Galeria
    path('entidad/galeria/<int:pk>', EntidadGaleriaView.as_view(), name='entidad_galeria'),
]
