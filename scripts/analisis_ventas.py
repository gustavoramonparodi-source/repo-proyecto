# =====================================================
# ANÁLISIS DE VENTAS - Escenario B
# Trabajo Práctico - Organización Empresarial
# =====================================================

import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------------------------------
# PASO 1: CARGAR EL ARCHIVO DE VENTAS
# Leemos el CSV que está en la carpeta /datos.
# -------------------------------------------------------

ruta_datos = "../datos/ventas.csv"
ruta_resultados = "../resultados"

# Crear la carpeta resultados si no existe
os.makedirs(ruta_resultados, exist_ok=True)

# Cargar el dataset
df = pd.read_csv(ruta_datos, parse_dates=["fecha_venta"])

print("Archivo cargado correctamente.")
print(df.head())

# -------------------------------------------------------
# PASO 2: CALCULAR INDICADORES
# Multiplicamos cantidad por precio para obtener
# el ingreso real de cada venta.
# -------------------------------------------------------

df["total"] = df["cantidad"] * df["precio_unitario"]

# Ventas totales
total = df["total"].sum()
print(f"\nVentas totales: $ {total:,.0f}")

# Producto más vendido por unidades
mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()
print(f"Producto más vendido: {mas_vendido}")

# Ventas por mes
df["mes"] = df["fecha_venta"].dt.to_period("M")
por_mes = df.groupby("mes")["total"].sum()

print("\nVentas por mes:")
print(por_mes)

# -------------------------------------------------------
# PASO 3: GENERAR EL GRÁFICO
# Gráfico de barras simple con la evolución mensual.
# Se guarda como imagen en la carpeta /resultados.
# -------------------------------------------------------

plt.figure(figsize=(8, 4))
plt.bar([str(m) for m in por_mes.index], por_mes.values, color="#2E75B6")
plt.title("Ventas por Mes - 2024")
plt.xlabel("Mes")
plt.ylabel("Total ($)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(f"{ruta_resultados}/grafico_ventas.png")
plt.show()

print("\nGráfico guardado en /resultados.")
print("Análisis finalizado.")
