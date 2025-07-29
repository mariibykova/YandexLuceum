import pygame
import random
import sys

pygame.init()

# Размеры окна
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bomb Game")


BLACK = (0, 0, 0)

bomb_image = pygame.image.load("data\bomb.png")
explosion_image = pygame.image.load("data\boom.png")

# Размеры изображений
BOMB_WIDTH, BOMB_HEIGHT = bomb_image.get_size()
EXPLOSION_WIDTH, EXPLOSION_HEIGHT = explosion_image.get_size()

# Класс Bomb
class Bomb:
    def __init__(self):
        self.x = random.randint(0, WIDTH - BOMB_WIDTH)
        self.y = random.randint(0, HEIGHT - BOMB_HEIGHT)
        self.image = bomb_image
        self.exploded = False

    def draw(self):
        if not self.exploded:
            screen.blit(self.image, (self.x, self.y))
        else:
            screen.blit(explosion_image, (self.x, self.y))

    def is_clicked(self, mouse_x, mouse_y):
        return (self.x <= mouse_x <= self.x + BOMB_WIDTH and
                self.y <= mouse_y <= self.y + BOMB_HEIGHT)

    def explode(self):
        self.exploded = True


bombs = [Bomb() for _ in range(20)]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for bomb in bombs:
                if bomb.is_clicked(mouse_x, mouse_y):
                    bomb.explode()


    screen.fill(BLACK)
    for bomb in bombs:
        bomb.draw()
        
    pygame.display.flip()


pygame.quit()
sys.exit()
