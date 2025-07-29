import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QRadioButton
from PyQt6.QtCore import Qt


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Крестики-нолики (3&times;3)")
        self.setFixedSize(300, 300)
        self.current_player = "X"
        self.game_finished = False
        self.x_radio = QRadioButton("X", self)
        self.x_radio.setGeometry(200, 20, 40, 20)
        self.x_radio.setChecked(True)
        self.x_radio.toggled.connect(self.handleFirstPlayerChange)

        self.o_radio = QRadioButton("O", self)
        self.o_radio.setGeometry(240, 20, 40, 20)

        self.new_game_button = QPushButton("Новая игра", self)
        self.new_game_button.setGeometry(10, 230, 100, 30)
        self.new_game_button.clicked.connect(self.startNewGame)
        self.result = QLabel("", self)
        self.result.setGeometry(10, 190, 280, 30)
        self.result.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )
        self.button_grid = []
        button_size = 50
        spacing = 10
        start_x = 10
        start_y = 10

        for row in range(3):
            row_buttons = []
            for col in range(3):
                btn = QPushButton("", self)
                btn.setGeometry(
                    start_x + col * (button_size + spacing),
                    start_y + row * (button_size + spacing) + 50,
                    button_size,
                    button_size,
                )
                btn.setText("")
                btn.clicked.connect(
                    lambda _, r=row, c=col: self.handleButtonClick(r, c)
                )
                row_buttons.append(btn)
            self.button_grid.append(row_buttons)
        self.startNewGame()

    def handleFirstPlayerChange(self):
        self.startNewGame()

    def startNewGame(self):
        if self.x_radio.isChecked():
            self.current_player = "X"
        else:
            self.current_player = "O"

        self.game_finished = False
        self.result.setText("")

        for row in range(3):
            for col in range(3):
                self.button_grid[row][col].setText("")
                self.button_grid[row][col].setEnabled(True)

    def handleButtonClick(self, row, col):
        if self.game_finished:
            return

        button = self.button_grid[row][col]
        if button.text() == "":
            button.setText(self.current_player)
            self.checkWinCondition()
            if not self.game_finished:
                self.switchPlayer()

    def switchPlayer(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def checkWinCondition(self):
        for row in range(3):
            if (
                self.button_grid[row][0].text() != ""
                and self.button_grid[row][0].text()
                == self.button_grid[row][1].text()
                == self.button_grid[row][2].text()
            ):
                self.showWinMessage(self.button_grid[row][0].text())
                return
        for col in range(3):
            if (
                self.button_grid[0][col].text() != ""
                and self.button_grid[0][col].text()
                == self.button_grid[1][col].text()
                == self.button_grid[2][col].text()
            ):
                self.showWinMessage(self.button_grid[0][col].text())
                return
        if (
            self.button_grid[0][0].text() != ""
            and self.button_grid[0][0].text()
            == self.button_grid[1][1].text()
            == self.button_grid[2][2].text()
        ):
            self.showWinMessage(self.button_grid[0][0].text())
            return
        if (
            self.button_grid[0][2].text() != ""
            and self.button_grid[0][2].text()
            == self.button_grid[1][1].text()
            == self.button_grid[2][0].text()
        ):
            self.showWinMessage(self.button_grid[0][2].text())
            return
        all_filled = True
        for row in range(3):
            for col in range(3):
                if self.button_grid[row][col].text() == "":
                    all_filled = False
                    break
            if not all_filled:
                break

        if all_filled:
            self.showDrawMessage()

    def showWinMessage(self, winner):
        self.game_finished = True
        self.result.setText(f"Выиграл {winner}!")
        self.blockField()

    def showDrawMessage(self):
        self.game_finished = True
        self.result.setText("Ничья!")
        self.blockField()

    def blockField(self):
        for row in range(3):
            for col in range(3):
                self.button_grid[row][col].setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec())
