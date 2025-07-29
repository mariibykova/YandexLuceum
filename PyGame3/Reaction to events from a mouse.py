import pygame

pygame.init()
size = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Реакция на события от мыши")


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.colors = [
            pygame.Color(0, 0, 0),
            pygame.Color(255, 0, 0),
            pygame.Color(0, 0, 255),
        ]
        self.current_color = 0

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
                pygame.draw.rect(
                    screen,
                    self.colors[self.board[y][x]],
                    (
                        x * self.cell_size + self.left + 1,
                        y * self.cell_size + self.top + 1,
                        self.cell_size - 2,
                        self.cell_size - 2,
                    ),
                )

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        x -= self.left
        y -= self.top
        if x < 0 or y < 0:
            return None
        col = x // self.cell_size
        row = y // self.cell_size
        if col >= self.width or row >= self.height:
            return None
        return row, col

    def on_click(self, cell):
        if cell is None:
            return
        row, col = cell
        self.board[row][col] = (self.board[row][col] + 1) % 3

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


board = Board(5, 7)
board.set_view(100, 100, 50)

r = True
while r:
    for el in pygame.event.get():
        if el.type == pygame.QUIT:
            r = False
        elif el.type == pygame.MOUSEBUTTONDOWN and el.button == 1:
            board.get_click(el.pos)

    board.render()
    pygame.display.flip()

pygame.quit()