
# urls.py
from django.contrib import admin
from django.urls import path

from aplicattion.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comentarios/', comentario_view, name='comentario_view'),
    path('',hello),
    path('formdpto/', formu_dpto),
    path('formmpio/', formu_mpio),
    path('formsuc/', formu_suc),
    path('formcli/', formu_cliente),
    path('formprenda/', formu_prenda),
    path('formarmario/', formu_armario),
    path('formfacturas/', formu_factura),
    path('formlavadoras/', formu_lavadora),
    path('bienvenida/', botones),
    path('departamentosl/', departamentos_list, name='departamentos_list'),
    path('municipios_list/', municipios_list),
    path('sucursalesl/', sucursales_list),
    path('clientes_list/', clientes_list),
    path('prendas_list/', prendas_list),
    path('facturasl/', facturas_list),
    path('form_factura/', fact_clie),
 

]
