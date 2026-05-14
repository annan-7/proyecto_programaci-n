import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np

# Carga inicial
data = np.load("VT__672.npy")

fig, ax = plt.subplots()

# espacio para botones
plt.subplots_adjust(bottom=0.25)

# datos iniciales (asegura eje x)
_x = np.arange(len(data))
linea, = ax.plot(_x, data)

ax.set_title("Señal de vibración")
ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Amplitud")
ax.grid()

texto_box = ax.text(
        0.02,
        0.95,
        "VT__672.npy",
        transform=ax.transAxes,
        verticalalignment="top",
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.9)
    )

def make_loader(filename):
    def on_click(event):
        try:
            senal = np.load(filename)
        except Exception as e:
            texto_box.set_text(f"Error cargando {filename}: {e}")
            plt.draw()
            return
        x = np.arange(len(senal))
        linea.set_xdata(x)
        linea.set_ydata(senal)
        linea.set_label(filename)
        ax.relim()
        ax.autoscale_view()
        ax.legend()
        texto_box.set_text(filename)
        plt.draw()
    return on_click


ax_btn1 = plt.axes([0.10, 0.05, 0.2, 0.08])
ax_btn2 = plt.axes([0.20, 0.05, 0.2, 0.08])
ax_btn3 = plt.axes([0.30, 0.05, 0.2, 0.08])
ax_btn4 = plt.axes([0.40, 0.05, 0.2, 0.08])
ax_btn5 = plt.axes([0.50, 0.05, 0.2, 0.08])

btn_VT_672 = Button(ax_btn1, "VT__672")
btn_VT_673 = Button(ax_btn2, "VT__673")
btn_VT_674 = Button(ax_btn3, "VT__674")
btn_VT_677 = Button(ax_btn4, "VT__677")
btn_VT_679 = Button(ax_btn5, "VT__679")


btn_VT_672.on_clicked(make_loader("VT__672.npy"))
btn_VT_673.on_clicked(make_loader("VT__673.npy"))
btn_VT_674.on_clicked(make_loader("VT__674.npy"))
btn_VT_677.on_clicked(make_loader("VT__677.npy"))
btn_VT_679.on_clicked(make_loader("VT__679.npy"))

plt.show()

suma_valores= np.sum(data)
num_valores = len(data)
promedio_senal = suma_valores / num_valores
datos_alcuadrado= np.sum((data - promedio_senal)**2)
varianza = datos_alcuadrado / num_valores
desviacion_estandar = np.sqrt(varianza)
