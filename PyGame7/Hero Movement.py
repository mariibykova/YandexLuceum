import pygame
import sys
import os

file_name = 'map.txt'


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def load_level(filename):
    filename = "data/" + filename
    try:
        with open(filename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]
        max_width = max(map(len, level_map))
        return list(map(lambda x: x.ljust(max_width, '.'), level_map))
    except OSError:
        print('Такого файла не существует')
        exit(0)


fps = 50
pygame.init()
pygame.display.set_caption('Перемещение героя.Камера')
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')
}
player_image = load_image('mario.png')
tile_width = tile_height = 50
player = None
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    return new_player, x, y


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(fps)


start_screen()
camera = Camera()

LEVEL = load_level(file_name)
for i in range(len(LEVEL)):
    if '@' in LEVEL[i]:
        x, y = i, LEVEL[i].index('@')
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if x == 0:
                    break
                if LEVEL[x - 1][y] == '.':
                    LEVEL[x] = LEVEL[x][:y] + '.' + LEVEL[x][y + 1:]
                    x -= 1
                    LEVEL[x] = LEVEL[x][:y] + '@' + LEVEL[x][y + 1:]
            elif event.key == pygame.K_DOWN:
                if x == len(LEVEL) - 1:
                    break
                if LEVEL[x + 1][y] == '.':
                    LEVEL[x] = LEVEL[x][:y] + '.' + LEVEL[x][y + 1:]
                    x += 1
                    LEVEL[x] = LEVEL[x][:y] + '@' + LEVEL[x][y + 1:]
            elif event.key == pygame.K_LEFT:
                if y == 0:
                    break
                if LEVEL[x][y - 1] == '.':
                    LEVEL[x] = LEVEL[x][:y] + '.' + LEVEL[x][y + 1:]
                    y -= 1
                    LEVEL[x] = LEVEL[x][:y] + '@' + LEVEL[x][y + 1:]
            else:
                if y == len(LEVEL[0]) - 1:
                    break
                if LEVEL[x][y + 1] == '.':
                    LEVEL[x] = LEVEL[x][:y] + '.' + LEVEL[x][y + 1:]
                    y += 1
                    LEVEL[x] = LEVEL[x][:y] + '@' + LEVEL[x][y + 1:]
    all_sprites = pygame.sprite.Group()
    player, level_x, level_y = generate_level(LEVEL)
    camera.update(player)
    for sprite in all_sprites:
        camera.apply(sprite)
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()