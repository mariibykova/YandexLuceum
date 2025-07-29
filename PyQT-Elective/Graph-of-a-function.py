import sys
import numpy as np
import pyqtgraph as pg
from PyQt6 import QtWidgets, QtCore


class FunctionPlotter(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QtWidgets.QVBoxLayout()
        self.function_input = QtWidgets.QLineEdit(self)
        self.function_input.setPlaceholderText("Введите функцию, например: np.sin(x)")
        layout.addWidget(self.function_input)
        self.range_start = QtWidgets.QLineEdit(self)
        self.range_start.setPlaceholderText("Начало диапазона")
        layout.addWidget(self.range_start)
        self.range_end = QtWidgets.QLineEdit(self)
        self.range_end.setPlaceholderText("Конец диапазона")
        layout.addWidget(self.range_end)
        self.plot_button = QtWidgets.QPushButton("Построить график", self)
        self.plot_button.clicked.connect(self.plot_function)
        layout.addWidget(self.plot_button)
        self.plot_widget = pg.PlotWidget()
        layout.addWidget(self.plot_widget)
        self.setLayout(layout)
        self.setWindowTitle("Построение графика функции")
        self.setGeometry(100, 100, 800, 600)

    def plot_function(self):
        try:
            function_text = self.function_input.text()
            start = float(self.range_start.text())
            end = float(self.range_end.text())
            x = np.linspace(start, end, 1000)
            y = eval(function_text, {"np": np, "x": x})
            self.plot_widget.clear()
            self.plot_widget.plot(x, y, pen="b")

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Ошибка", str(e))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FunctionPlotter()
    window.show()
    sys.exit(app.exec())
