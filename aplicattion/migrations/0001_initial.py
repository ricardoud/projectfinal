# Generated by Django 4.2.16 on 2024-11-16 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="armario",
            fields=[
                ("id_armario", models.AutoField(primary_key=True, serialize=False)),
                ("ubicacion", models.CharField(max_length=40)),
                ("capacidad", models.IntegerField(max_length=10)),
                ("estado", models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name="cliente",
            fields=[
                (
                    "identificacion",
                    models.IntegerField(
                        max_length=20, primary_key=True, serialize=False
                    ),
                ),
                ("nombre1", models.CharField(max_length=40)),
                ("nombre2", models.CharField(max_length=40)),
                ("apellido1", models.CharField(max_length=40)),
                ("apellido2", models.CharField(max_length=40)),
                ("email", models.EmailField(max_length=70)),
                ("telefono", models.CharField(max_length=10)),
                ("direccion", models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name="departamento",
            fields=[
                (
                    "cod_dpto",
                    models.CharField(max_length=2, primary_key=True, serialize=False),
                ),
                ("nombre_dpto", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="factura",
            fields=[
                ("id_factura", models.AutoField(primary_key=True, serialize=False)),
                ("estado", models.CharField(max_length=12)),
                ("fecha_emision", models.DateTimeField()),
                ("valor_total", models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="lavadora",
            fields=[
                ("id_lavadora", models.AutoField(primary_key=True, serialize=False)),
                ("marca", models.CharField(max_length=20)),
                ("capacidad", models.IntegerField(max_length=10)),
                ("modelo", models.IntegerField(max_length=4)),
                ("estado", models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name="municipio",
            fields=[
                (
                    "cod_mpio",
                    models.CharField(max_length=3, primary_key=True, serialize=False),
                ),
                ("nombre_mun", models.CharField(max_length=200)),
                (
                    "nombre_dpto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="aplicattion.departamento",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="prenda",
            fields=[
                ("id_prenda", models.AutoField(primary_key=True, serialize=False)),
                ("descripcion", models.CharField(max_length=40)),
                ("color", models.CharField(max_length=40)),
                ("estado", models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name="sucursal",
            fields=[
                (
                    "sucursal_id",
                    models.IntegerField(
                        max_length=5, primary_key=True, serialize=False
                    ),
                ),
                ("direccion", models.CharField(max_length=200)),
                (
                    "cod_mun",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="aplicattion.municipio",
                    ),
                ),
            ],
        ),
    ]
