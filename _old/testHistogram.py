import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget
from PyQt5.QtGui import QPixmap, QImage
import sys

class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

def plot_color_histogram(image_path, canvas):
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    hist_r = cv2.calcHist([img_rgb], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([img_rgb], [1], None, [256], [0, 256])
    hist_b = cv2.calcHist([img_rgb], [2], None, [256], [0, 256])

    canvas.ax.plot(hist_r, color='red', label='R', linewidth=2)
    canvas.ax.plot(hist_g, color='green', label='G', linewidth=2)
    canvas.ax.plot(hist_b, color='blue', label='B', linewidth=2)

    canvas.ax.set_title('Histogram barev')
    canvas.ax.set_xlabel('Intenzita barev')
    canvas.ax.set_ylabel('Počet pixelů')
    canvas.ax.legend()

    canvas.draw()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.image_path = 'path/to/your/image.jpg'
        self.canvas = MatplotlibCanvas(self, width=5, height=4, dpi=100)
        self.layout.addWidget(self.canvas)

        self.plot_color_histogram()

    def plot_color_histogram(self):
        plot_color_histogram(self.image_path, self.canvas)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())