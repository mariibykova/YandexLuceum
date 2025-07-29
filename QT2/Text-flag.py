import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QButtonGroup,
    QRadioButton,
    QPushButton,
    QLabel,
)
from PyQt6.QtCore import Qt


class FlagMaker(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(400, 300)
        self.setWindowTitle("Текстовый флаг")
        self.color_group_1 = QButtonGroup(self)

        self.blue_radio_1 = QRadioButton("Синий", self)
        self.blue_radio_1.move(30, 30)
        self.blue_radio_1.setChecked(True)
        self.color_group_1.addButton(self.blue_radio_1)

        self.red_radio_1 = QRadioButton("Красный", self)
        self.red_radio_1.move(30, 60)
        self.color_group_1.addButton(self.red_radio_1)

        self.green_radio_1 = QRadioButton("Зелёный", self)
        self.green_radio_1.move(30, 90)
        self.color_group_1.addButton(self.green_radio_1)

        self.color_group_2 = QButtonGroup(self)

        self.blue_radio_2 = QRadioButton("Синий", self)
        self.color_group_2.addButton(self.blue_radio_2)
        self.blue_radio_2.move(150, 30)

        self.red_radio_2 = QRadioButton("Красный", self)
        self.color_group_2.addButton(self.red_radio_2)
        self.red_radio_2.move(150, 60)
        self.red_radio_2.setChecked(True)

        self.green_radio_2 = QRadioButton("Зелёный", self)
        self.color_group_2.addButton(self.green_radio_2)
        self.green_radio_2.move(150, 90)

        self.color_group_3 = QButtonGroup(self)

        self.blue_radio_3 = QRadioButton("Синий", self)
        self.color_group_3.addButton(self.blue_radio_3)
        self.blue_radio_3.move(270, 30)

        self.red_radio_3 = QRadioButton("Красный", self)
        self.color_group_3.addButton(self.red_radio_3)
        self.red_radio_3.move(270, 60)

        self.green_radio_3 = QRadioButton("Зелёный", self)
        self.color_group_3.addButton(self.green_radio_3)
        self.green_radio_3.move(270, 90)
        self.green_radio_3.setChecked(True)

        self.make_flag = QPushButton("Сделать флаг", self)
        self.make_flag.move(150, 140)
        self.make_flag.clicked.connect(self.generate_flag)

        self.result = QLabel("", self)
        self.result.setObjectName("result")
        self.result.move(30, 200)
        self.result.resize(340, 40)
        self.result.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def generate_flag(self):
        color_1 = self.get_selected_color(self.color_group_1)
        color_2 = self.get_selected_color(self.color_group_2)
        color_3 = self.get_selected_color(self.color_group_3)
        flag_text = f"Цвета: {color_1}, {color_2} и {color_3}"
        self.result.setText(flag_text)

    def get_selected_color(self, group: QButtonGroup) -> str:
        checked = group.checkedButton()
        return checked.text() if checked else ""


def main():
    app = QApplication(sys.argv)
    window = FlagMaker()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
