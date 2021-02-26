import pygame
import sys
from os import path

KEY_SIZE = 128

NCOLS = 4
NROWS = 3

APP_WIDTH = KEY_SIZE * NCOLS + 16
APP_HEIGHT = KEY_SIZE * NROWS + 16
APP_SIZE = (APP_WIDTH, APP_HEIGHT)

BG_COLOR = (255, 255, 255)

pygame.init()
app = pygame.display.set_mode(APP_SIZE)

def load_image(source):
    return pygame.image.load(path.join('images', source)).convert_alpha()

class Key(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.up_img = load_image('key_black1.png')
        self.down_img = load_image('key_black2.png')
        self.image = self.up_img
        self.rect = self.image.get_rect()

def quit():
    pygame.quit()
    sys.exit()

matrix = [[] for i in range(NCOLS)]
keys = pygame.sprite.Group()

for col in range(NCOLS):
    for row in range(NROWS):
        key = Key()
        key.rect.topleft = (KEY_SIZE * col + 16, KEY_SIZE * row + 16)
        matrix[col].append(key)
        keys.add(key)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                quit()
    app.fill(BG_COLOR)
    keys.draw(app)
    pygame.display.flip()
