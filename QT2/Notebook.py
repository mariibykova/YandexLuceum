import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QListWidget
)


class MyNotes(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 300)
        self.setWindowTitle("Записная книжка")
        self.contactName = QLineEdit(self)
        self.contactName.setObjectName("contactName")
        self.contactName.setPlaceholderText("Имя контакта")
        self.contactName.setGeometry(20, 20, 180, 30)
        self.contactNumber = QLineEdit(self)
        self.contactNumber.setObjectName("contactNumber")
        self.contactNumber.setPlaceholderText("Телефон")
        self.contactNumber.setGeometry(20, 60, 180, 30)
        self.addContactBtn = QPushButton("Добавить контакт", self)
        self.addContactBtn.setObjectName("addContactBtn")
        self.addContactBtn.setGeometry(220, 20, 150, 30)
        self.addContactBtn.clicked.connect(self.add_contact)
        self.contactList = QListWidget(self)
        self.contactList.setObjectName("contactList")
        self.contactList.setGeometry(20, 110, 350, 160)

    def add_contact(self):
        name = self.contactName.text().strip()
        number = self.contactNumber.text().strip()

        if name and number:
            self.contactList.addItem(f"{name} {number}")

        self.contactName.clear()
        self.contactNumber.clear()


def main():
    app = QApplication(sys.argv)
    window = MyNotes()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
