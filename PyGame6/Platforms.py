import pygame
import sys

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)

GRAVITY = 5


class Platform:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 10)

    def draw(self, screen):
        pygame.draw.rect(screen, GRAY, self.rect)


class Character:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.velocity_y = 0

    def update(self, platforms, dt):
        self.velocity_y += GRAVITY * dt
        self.rect.y += self.velocity_y
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                self.rect.bottom = platform.rect.top
                self.velocity_y = 0

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, self.rect)

    def move(self, dx):
        self.rect.x += dx


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.platforms = []
        self.character = None

    def run(self):
        while True:
            dt = self.clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = event.pos
                        self.platforms.append(Platform(x - 25, y - 5))
                    elif event.button == 3:
                        x, y = event.pos
                        if self.character:
                            self.character.rect.topleft = (x - 10, y - 10)
                        else:
                            self.character = Character(x - 10, y - 10)
                if event.type == pygame.KEYDOWN:
                    if self.character:
                        if event.key == pygame.K_LEFT:
                            self.character.move(-10)
                        elif event.key == pygame.K_RIGHT:
                            self.character.move(10)
            if self.character:
                self.character.update(self.platforms, dt)

            self.screen.fill(BLACK)
            for platform in self.platforms:
                platform.draw(self.screen)
            if self.character:
                self.character.draw(self.screen)

            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
