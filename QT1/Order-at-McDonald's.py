import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QCheckBox,
    QPushButton,
    QPlainTextEdit,
)
from PyQt6.QtCore import Qt


class MacOrder(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Заказ в Макдональдсе")
        self.setGeometry(100, 100, 300, 300)
        menu_items = ["Чизбургер", "Гамбургер", "Кока-кола", "Наггетсы"]
        self.menu_checkboxes = []
        checkbox_y = 20
        for item in menu_items:
            cb = QCheckBox(item, self)
            cb.move(20, checkbox_y)
            checkbox_y += 30
            self.menu_checkboxes.append(cb)

        self.order_btn = QPushButton("Заказать", self)
        self.order_btn.move(20, checkbox_y + 10)
        self.order_btn.resize(100, 30)
        self.order_btn.clicked.connect(self.show_order)

        self.result = QPlainTextEdit(self)
        self.result.setReadOnly(True)
        self.result.move(150, 20)
        self.result.resize(130, 200)

    def show_order(self):
        order_text = "Ваш заказ:\n\n"
        for cb in self.menu_checkboxes:
            if cb.isChecked():
                order_text += cb.text() + "\n"

        self.result.setPlainText(order_text)


def main():
    app = QApplication(sys.argv)
    window = MacOrder()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
