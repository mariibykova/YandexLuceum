import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton


class WidgetArt(QWidget):
    def __init__(self, matrix):
        super().__init__()
        self.matrix = matrix
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Widget Art")
        self.widgetArt = QGridLayout()
        self.widgetArt.setObjectName("widgetArt")
        for ind, i in enumerate(self.matrix):
            for col_ind, val in enumerate(i):
                btn = QPushButton("*" if val == 1 else "")
                self.widgetArt.addWidget(btn, ind, col_ind)
        self.setLayout(self.widgetArt)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    matrix = [
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    ]

    ex = WidgetArt(matrix)
    ex.show()

    sys.exit(app.exec())
