from django.db import models


class Cliente(models.Model):
    cedula = models.CharField(max_length=20)
    nombres = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    direccion = models.TextField(max_length=200)
    celular = models.CharField(max_length=20)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.cedula}"
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre =  models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=1000, decimal_places=2)
    descripcion = models.TextField()
    stock = models.IntegerField(default=0)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='productos', null=True, blank=True)
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE, related_name='productos', null=True, blank=True)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.precio}"
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length= 100)
    apellidos = models.CharField(max_length=100)
    direccion = models.TextField()
    celular = models.CharField(max_length=20)
    cedula_ruc = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} {self.apellidos} - {self.cedula_ruc}"
    
class Modelo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}"
    
class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE, related_name='marcas')

    def __str__(self):
        return f"{self.nombre}"
    

class Reserva(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='reservas')
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, related_name='reservas')
    monto_total = models.DecimalField(max_digits=1000, decimal_places=2)
    cuotas_pagadas = models.IntegerField(default=0)
    monto_restante = models.DecimalField(max_digits=1000, decimal_places=2)
    fecha_reserva = models.DateField(auto_now_add=True)    
    
    def __str__(self):
        return f"Reserva de {self.cliente.nombres} para {self.producto.nombre}"
    
class Cuota(models.Model):
    reserva = models.ForeignKey('Reserva', on_delete=models.CASCADE, related_name='cuotas')
    fecha = models.DateField(auto_now_add=True)
    monto = models.DecimalField(max_digits=1000, decimal_places=2)
    subtotal_aportado = models.DecimalField(max_digits=1000, decimal_places=2)
    
    def __str__(self):
        return f"Cuota de {self.monto} para la reserva de {self.reserva.cliente.nombres}"
    
class Factura(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='facturas')
    fecha = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=1000, decimal_places=2)

    def __str__(self):
        return f"Factura {self.id} - {self.cliente.nombres} ({self.fecha})"
    
class LineaFactura(models.Model):
    factura = models.ForeignKey('Factura', on_delete=models.CASCADE, related_name='lineas')
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, related_name='lineas')
    cantidad = models.IntegerField(default=1)
    subtotal = models.DecimalField(max_digits=1000, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en Factura {self.factura.id}"