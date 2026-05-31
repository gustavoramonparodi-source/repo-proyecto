Análisis de Ventas — Trabajo Práctico UTN 

**Materia:** Organización Empresarial  
**Institución:** Universidad Tecnológica Nacional — Tecnicatura Universitaria en Programación (TUP) — Modalidad a Distancia  
**Año Lectivo:** 2026

---

# Integrantes del Equipo

| Rol | gustavo
|-----|--------|-----------------|
| P1 – Líder y Organizador (Hugo) | [gustavo | Gobernanza del repositorio, estructura de carpetas y README |
| P2 – Desarrollador Técnico (Paco) | [gustavo] | Script Python de análisis estadístico |
| P3 – Revisor y QA (Luis) | [gustavo] | Documentación, revisión de código y Pull Requests |

---

# Escenario Elegido

**Escenario B – Análisis de Ventas de una Pequeña Empresa**

El proyecto analiza un conjunto de datos simulados de ventas comerciales para generar indicadores básicos de desempeño: ventas totales, producto más vendido y evolución mensual de ingresos.

---

# Estructura del Repositorio
```
repo-proyecto/
│
├── datos/
│   └── ventas.csv              # Dataset de ventas simuladas (30 registros, 6 meses)
│
├── scripts/
│   └── analisis_ventas.py      # Script Python de análisis estadístico
│
├── resultados/
│   ├── grafico_ventas_mensuales.png   # Gráfico de evolución mensual (generado por el script)
│   └── resumen_indicadores.txt        # Resumen en texto de los indicadores calculados
│
├── README.md                   # Este archivo
└── .gitignore                  # Exclusión de archivos temporales y sensibles
```

---

# Dataset Utilizado

**Archivo:** `datos/ventas.csv`  
**Fuente:** Dataset simulado generado para actividades educativas  
**Período:** Enero 2024 – Junio 2024  
**Registros:** 30 transacciones de venta  

**Columnas:**
| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | Entero | Identificador único de la transacción |
| `producto` | Texto | Nombre del producto vendido |
| `cantidad` | Entero | Unidades vendidas |
| `precio_unitario` | Entero | Precio por unidad en pesos argentinos |
| `fecha_venta` | Fecha | Fecha de la transacción (YYYY-MM-DD) |

**Productos incluidos:** Notebook, Mouse, Teclado, Monitor, Auriculares

---

# Cómo Ejecutar el Script en Google Colab

1. Abrir [Google Colab](https://colab.research.google.com/)
2. Crear una nueva notebook
3. Clonar el repositorio:
``python
!git clone https://github.com/TU_USUARIO/repo-proyecto.git
```
4. Ejecutar el script:
python
!python repo-proyecto/scripts/analisis_ventas.py
```
5. Los resultados se guardarán automáticamente en la carpeta `resultados/`

---

# Indicadores Generados

El script calcula y reporta:
- **Ventas totales** en el período analizado
- **Producto más vendido** por volumen de unidades
- **Producto con mayor ingreso** monetario
- **Ventas por mes** (evolución temporal)
- **Gráfico de barras** con la evolución mensual de ventas

---

#Gestión del Proyecto

- **Tablero Jira:** [Enlace al tablero]
- **Repositorio GitHub:** [Enlace al repositorio]

---

Trazabilidad de Commits

Todos los commits siguen el formato de Conventional Commits con ID de Issue de Jira:

```
PROY-1: Agregar estructura inicial de carpetas y README
PROY-2: Agregar dataset de ventas simuladas en /datos
PROY-3: Agregar script de análisis estadístico en /scripts
PROY-4: Agregar archivo .gitignore
PROY-5: Corregir rutas relativas en script de análisis
```
