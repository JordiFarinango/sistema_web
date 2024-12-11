from django.contrib import admin
from .models import Cliente, Producto, Proveedor, Categoria, Marca, Reserva, Cuota, Factura, LineaFactura

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Reserva)
admin.site.register(Cuota)
admin.site.register(Factura)
admin.site.register(LineaFactura)
