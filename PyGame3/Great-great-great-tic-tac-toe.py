import pygame

pygame.init()
size = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Пра-пра-пра-крестики-нолики")


class Board:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.board = [[None] * w for _ in range(h)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.current_player = "X"

    def render(self):
        screen.fill((0, 0, 0))
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(
                    screen,
                    pygame.Color(255, 255, 255),
                    (
                        x * self.cell_size + self.left,
                        y * self.cell_size + self.top,
                        self.cell_size,
                        self.cell_size,
                    ),
                    1,
                )
                if self.board[y][x] == "X":
                    self.draw_x(x, y)
                elif self.board[y][x] == "O":
                    self.draw_o(x, y)

    def draw_x(self, x, y):
        pygame.draw.line(
            screen,
            pygame.Color(0, 0, 255),
            (x * self.cell_size + self.left + 2, y * self.cell_size + self.top + 2),
            (
                (x + 1) * self.cell_size + self.left - 2,
                (y + 1) * self.cell_size + self.top - 2,
            ),
            2,
        )
        pygame.draw.line(
            screen,
            pygame.Color(0, 0, 255),
            (
                (x + 1) * self.cell_size + self.left - 2,
                y * self.cell_size + self.top + 2,
            ),
            (
                x * self.cell_size + self.left + 2,
                (y + 1) * self.cell_size + self.top - 2,
            ),
            2,
        )

    def draw_o(self, x, y):
        pygame.draw.circle(
            screen,
            pygame.Color(255, 0, 0),
            (
                x * self.cell_size + self.left + self.cell_size // 2,
                y * self.cell_size + self.top + self.cell_size // 2,
            ),
            self.cell_size // 2 - 2,
            2,
        )

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def on_click(self, cell):
        x = cell[0] - self.left
        y = cell[1] - self.top
        row = y // self.cell_size
        col = x // self.cell_size

        if (
            0 <= row < self.height
            and 0 <= col < self.width
            and self.board[row][col] is None
        ):
            self.board[row][col] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"


board = Board(7, 5)
board.set_view(75, 100, 50)

r = True
while r:
    for el in pygame.event.get():
        if el.type == pygame.QUIT:
            r = False
        elif el.type == pygame.MOUSEBUTTONDOWN and el.button == 1:
            board.on_click(el.pos)
    board.render()
    pygame.display.flip()

pygame.quit()
