
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

]
