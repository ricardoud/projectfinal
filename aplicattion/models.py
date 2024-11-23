from django.db import models

# Create your models here.

class departamento (models.Model):
    cod_dpto=models.CharField(max_length=2,primary_key=True)
    nombre_dpto=models.CharField(max_length=200, null=False)

class municipio (models.Model):
        cod_mpio=models.CharField(max_length=3,primary_key=True)
        nombre_mun=models.CharField(max_length=200, null=False)
        cod_dpto=models.ForeignKey(departamento, on_delete=models.CASCADE)

class sucursal (models.Model):
        sucursal_id=models.IntegerField(max_length=5,primary_key=True)
        direccion=models.CharField(max_length=200, null=False)
        cod_mun=models.ForeignKey(municipio, on_delete=models.CASCADE)

class cliente (models.Model):
        identificacion=models.IntegerField(max_length=20,primary_key=True)
        nombre1=models.CharField(max_length=40, null=False)
        nombre2=models.CharField(max_length=40, null=False)
        apellido1=models.CharField(max_length=40, null=False)
        apellido2=models.CharField(max_length=40, null=False)
        email=models.EmailField(max_length=70, null=False)
        telefono=models.CharField(max_length=10, null=False)
        direccion=models.CharField(max_length=60, null=False)

class prenda (models.Model):
        id_prenda = models.AutoField(primary_key=True)
        descripcion=models.CharField(max_length=40, null=False)
        color=models.CharField(max_length=40, null=False)
        estado=models.CharField(max_length=12, null=False)

class armario (models.Model):
        id_armario = models.AutoField(primary_key=True)
        ubicacion=models.CharField(max_length=40, null=False)
        capacidad=models.IntegerField(max_length=10, null=False)
        estado=models.CharField(max_length=12, null=False)

class factura (models.Model):
        id_factura = models.AutoField(primary_key=True)
        estado=models.CharField(max_length=12, null=False)
        fecha_emision=models.DateTimeField(null=False)
        valor_total=models.IntegerField(max_length=20, null=False)

class lavadora (models.Model):
        id_lavadora = models.AutoField(primary_key=True)
        marca=models.CharField(max_length=20, null=False)
        capacidad=models.IntegerField(max_length=10, null=False)
        modelo=models.IntegerField(max_length=4, null=False)
        estado=models.CharField(max_length=12, null=False)


class fact_clie (models.Model):

        id_fact=models.ForeignKey(factura, on_delete=models.CASCADE)
        id_cliente=models.ForeignKey(cliente, on_delete=models.CASCADE)


        

