import pygame
import sys
 
try:
    n = int(input())
except:
    print('Неправильный формат ввода')
    sys.exit()
 
pygame.init()
pygame.display.set_caption('Сфера')
h = 300
w = 300
white = (255, 255, 255)
screen = pygame.display.set_mode((w, h))
s = 300 // n
pygame.draw.ellipse(screen, white, (0, 0, 300, 300), 1)
pygame.draw.ellipse(screen, white, (0, h // 2 - s // 2, 300, s), 1)
pygame.draw.ellipse(screen, white, (w // 2 - s // 2, 0, s, 300), 1)
 
for i in range(n - 1):
    pygame.draw.ellipse(screen, white, (0, h // 2 - s // 2 * (i + 1), 300, s * (i + 1)), 1)
    pygame.draw.ellipse(screen, white, (h // 2 - s // 2 * (i + 1), 0, s * (i + 1), 300), 1)
 
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
