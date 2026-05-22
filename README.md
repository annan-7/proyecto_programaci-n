# Proyecto 1: Análisis Interactivo de Señales Digitales

## Descripción

Aplicación desarrollada en Python para cargar, visualizar y analizar señales digitales almacenadas en archivos `.npy`.

El programa detecta automáticamente los archivos disponibles, permite seleccionar una señal y aplicar filtros de procesamiento mediante una interfaz gráfica interactiva creada con Matplotlib.

## Funcionalidades

- Detección automática de archivos `.npy`.
- Visualización de la señal original.
- Filtro de media móvil (ventana de 7 muestras).
- Filtro de mediana móvil (ventana de 7 muestras).
- Cálculo de estadísticas:
  - Valor máximo
  - Valor mínimo
  - Promedio
  - Desviación estándar

## Lib Utilizadas
- NumPy
- Matplotlib

## Ejecución

```bash
pip install numpy matplotlib
python main.py
