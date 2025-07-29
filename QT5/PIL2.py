import sys

from itertools import product
from copy import deepcopy

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QButtonGroup
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QImage, QTransform, QPixmap, qRgb


class MyPillow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(700, 250, 500, 500)
        self.setWindowTitle("PIL 2.0")

        file_name = QFileDialog.getOpenFileName(self, "Выбрать картинку", "")[0]
        self.original_image, self.curr_image = QImage(file_name), QImage(file_name)
        self.pixmap = QPixmap(self.curr_image.copy())

        self.image = QLabel(self)
        self.image.resize(250, 250)
        self.image.move(225, 25)
        self.image.setPixmap(self.pixmap)

        self.angle = 0
        self.color = "ALL"

        self.channelButtons = QButtonGroup()
        for index, name in enumerate(["R", "G", "B", "ALL"]):
            button = QPushButton(name, self)
            button.setGeometry(0, index * 75, 200, 50)
            button.clicked.connect(self.change_color)

            self.channelButtons.addButton(button)

        self.rotateButtons = QButtonGroup()
        for index, name in enumerate(["Против часовой стрелки", "По часовой стрелке"]):
            button = QPushButton(name, self)
            button.setGeometry(25 + index * 250, 325, 200, 50)
            button.clicked.connect(self.change_angle)

            self.rotateButtons.addButton(button)

    def change_color(self) -> None:
        self.color = self.sender().text()
        self.__show_image()

    def change_angle(self) -> None:
        flag = -1 if self.sender().text() == "Против часовой стрелки" else 1
        self.angle = (self.angle + 90 * flag) % 360
        self.__show_image()

    def __show_image(self) -> None:
        self.curr_image = self.original_image.copy()
        self.pixmap = QPixmap(self.curr_image.copy())

        if self.color != "ALL":
            x, y = self.pixmap.size().width(), self.pixmap.size().height()

            for i, j in product(range(x), range(y)):
                r, g, b, a = self.curr_image.pixelColor(i, j).getRgb()
                r, g, b = (
                    (self.color == "R") * r,
                    (self.color == "G") * g,
                    (self.color == "B") * b,
                )
                self.curr_image.setPixel(i, j, qRgb(r, g, b))

        self.curr_image = self.curr_image.transformed(QTransform().rotate(self.angle))
        self.pixmap = QPixmap(self.curr_image.copy())
        self.image.setPixmap(self.pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec())
