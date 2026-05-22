import glob
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button



# Buscar archivos

def buscar_archivos():
    return glob.glob("*.npy")



# Mostrar menú


def mostrar_menu(archivos):
    print("\nArchivos disponibles:\n")
    for i in range(len(archivos)):
        print(f"{i+1}. {archivos[i]}")
    opcion = int(input("\nSeleccione el archivo: "))
    while opcion < 1 or opcion > len(archivos):
        opcion = int(input("Opción inválida. Intente nuevamente: "))
    return opcion



# Cargar señal

def cargar_senal(nombre_archivo):
    return np.load(nombre_archivo)


# Media movil


def media_movil(datos):
    resultado = []
    for i in range(len(datos)):
        ventana = []
        for j in range(i - 3, i + 4):
            if 0 <= j < len(datos):
                ventana.append(datos[j])
        promedio = sum(ventana) / len(ventana)
        resultado.append(promedio)
    return resultado


# Mediana movil

def mediana_movil(datos):
    resultado = []
    for i in range(len(datos)):
        ventana = []
        for j in range(i - 3, i + 4):
            if 0 <= j < len(datos):
                ventana.append(datos[j])
        ventana.sort()
        mediana = ventana[len(ventana) // 2]
        resultado.append(mediana)
    return resultado



# Estadísticas


def calcular_estadisticas(datos):
    maximo = max(datos)
    minimo = min(datos)
    promedio = sum(datos) / len(datos)
    suma = 0
    for valor in datos:
        suma += (valor - promedio) ** 2
    desviacion = (suma / len(datos)) ** 0.5

    print("\n--- ESTADÍSTICAS ---")
    print("Máximo:", maximo)
    print("Mínimo:", minimo)
    print("Promedio:", promedio)
    print("Desviación estándar:", desviacion)



# Programa principal


archivos = buscar_archivos()

if len(archivos) == 0:
    print("No se encontraron archivos .npy")
    exit()

opcion = mostrar_menu(archivos)
nombre_archivo = archivos[opcion - 1]
senal_original = cargar_senal(nombre_archivo)
senal_actual = senal_original.copy()


# Gráfico


fig, ax = plt.subplots()

plt.subplots_adjust(bottom=0.30)

linea, = ax.plot(
    senal_original,
    label="Señal Original"
)

ax.set_title(f"Señal: {nombre_archivo}")
ax.set_xlabel("Muestras")
ax.set_ylabel("Amplitud")
ax.grid(True)
ax.legend()



# Actualizar gráfico


def actualizar_grafico(datos, titulo):
    global senal_actual
    senal_actual = datos

    linea.set_ydata(datos)
    linea.set_xdata(range(len(datos)))

    ax.relim()
    ax.autoscale_view()

    ax.set_title(titulo)

    fig.canvas.draw_idle()



# Eventos botones


def mostrar_original(event):
    actualizar_grafico(
        senal_original,
        f"Señal Original - {nombre_archivo}"
    )


def mostrar_media(event):
    datos_filtrados = media_movil(senal_original)
    actualizar_grafico(
        datos_filtrados,
        f"Media Móvil - {nombre_archivo}"
    )


def mostrar_mediana(event):
    datos_filtrados = mediana_movil(senal_original)
    actualizar_grafico(
        datos_filtrados,
        f"Mediana Móvil - {nombre_archivo}"
    )


def mostrar_estadisticas(event):
    calcular_estadisticas(senal_actual)



# Botones


ax_original = plt.axes([0.05, 0.1, 0.18, 0.08])
ax_media = plt.axes([0.28, 0.1, 0.18, 0.08])
ax_mediana = plt.axes([0.51, 0.1, 0.18, 0.08])
ax_estadisticas = plt.axes([0.74, 0.1, 0.18, 0.08])

btn_original = Button(ax_original, "Original")
btn_media = Button(ax_media, "Media Movil")
btn_mediana = Button(ax_mediana, "Mediana Movil")
btn_estadisticas = Button(ax_estadisticas, "Estadisticas")

btn_original.on_clicked(mostrar_original)
btn_media.on_clicked(mostrar_media)
btn_mediana.on_clicked(mostrar_mediana)
btn_estadisticas.on_clicked(mostrar_estadisticas)

plt.show()