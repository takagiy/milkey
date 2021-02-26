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

KEY_SEQ = 'wbwbwwbwbwbw'
R_KBD_SEQ = 'zxcvasdfqwer'

pygame.init()
pygame.display.set_caption('milkey')
app = pygame.display.set_mode(APP_SIZE)

def load_image(source):
    return pygame.image.load(path.join('images', source)).convert_alpha()

class Key(pygame.sprite.Sprite):
    def __init__(self, c):
        color = 'white' if c == 'w' else 'black'
        pygame.sprite.Sprite.__init__(self)
        self.up_img = load_image(f'key_{color}1.png')
        self.down_img = load_image(f'key_{color}2.png')
        self.image = self.up_img
        self.rect = self.image.get_rect()

def quit():
    pygame.quit()
    sys.exit()

matrix = []
keys = pygame.sprite.Group()

for row in range(NROWS):
    for col in range(NCOLS):
        color = KEY_SEQ[NCOLS * row + col]
        key = Key(color)
        key.rect.topleft = (KEY_SIZE * col + 16, KEY_SIZE * (NROWS - 1 - row) + 16)
        matrix.append(key)
        keys.add(key)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            try:
                keyid = R_KBD_SEQ.index(chr(event.key))
            except ValueError:
                continue
            key = matrix[keyid]
            key.image = key.down_img
        if event.type == pygame.KEYUP:
            try:
                keyid = R_KBD_SEQ.index(chr(event.key))
            except ValueError:
                continue
            key = matrix[keyid]
            key.image = key.up_img
    app.fill(BG_COLOR)
    keys.draw(app)
    pygame.display.flip()
