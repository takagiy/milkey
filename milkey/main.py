import pygame
import mido
import sys
from os import path

KEY_SIZE = 128

NCOLS = 4
NROWS = 4

MATRIX_WIDTH = KEY_SIZE * NCOLS + 8
MATRIX_HEIGHT = KEY_SIZE * NROWS + 8
R_MATRIX_X_OFFSET = MATRIX_WIDTH + 64

APP_WIDTH = MATRIX_WIDTH * 2 + 64
APP_HEIGHT = MATRIX_HEIGHT
APP_SIZE = (APP_WIDTH, APP_HEIGHT)

BG_COLOR = (255, 255, 255)

KEY_SEQ = 'wbwbwwbwbwbwwbwbw'
L_KBD_SEQ = 'zxcvasdfqwer1234'
R_KBD_SEQ = 'nm,.jkl;iop[90-='

PORT_NAME = 'loopMIDI Port 1'

def load_image_raw(source):
    return pygame.image.load(path.join('images', source))

def load_image(source):
    return load_image_raw(source).convert_alpha()

class Key(pygame.sprite.Sprite):
    def __init__(self, c):
        color = 'white' if c == 'w' else 'black'
        pygame.sprite.Sprite.__init__(self)
        self.up_img = load_image(f'key_{color}1.png')
        self.down_img = load_image(f'key_{color}2.png')
        self.image = self.up_img
        self.rect = self.image.get_rect()

def send_on(keyid):
    noteid = keyid + noteoffset
    message = mido.Message('note_on', note=noteid)
    port.send(message)

def send_off(keyid):
    noteid = keyid + noteoffset
    message = mido.Message('note_off', note=noteid)
    port.send(message)

def process_lpressed(key):
    try:
        keyid = L_KBD_SEQ.index(chr(event.key))
    except ValueError:
        return
    send_on(keyid)
    key = lmatrix[keyid]
    key.image = key.down_img

def process_lreleased(key):
    try:
        keyid = L_KBD_SEQ.index(chr(event.key))
    except ValueError:
        return
    send_off(keyid)
    key = lmatrix[keyid]
    key.image = key.up_img

def process_rpressed(key):
    try:
        keyid = R_KBD_SEQ.index(chr(event.key))
    except ValueError:
        return
    key = rmatrix[keyid]
    key.image = key.down_img

def process_rreleased(key):
    try:
        keyid = R_KBD_SEQ.index(chr(event.key))
    except ValueError:
        return
    key = rmatrix[keyid]
    key.image = key.up_img

def quit():
    pygame.quit()
    sys.exit()

pygame.init()
pygame.display.set_caption('milkey')
pygame.display.set_icon(load_image_raw('icon.png'))
app = pygame.display.set_mode(APP_SIZE)

port = mido.open_output(PORT_NAME)

noteoffset = 60

lmatrix = []
rmatrix = []
keys = pygame.sprite.Group()

for row in range(NROWS):
    for col in range(NCOLS):
        color = KEY_SEQ[NCOLS * row + col]
        for (matrix, xoffset) in [(lmatrix, 0), (rmatrix, R_MATRIX_X_OFFSET)]:
            key = Key(color)
            key.rect.topleft = (KEY_SIZE * col + 8 + xoffset, KEY_SIZE * (NROWS - 1 - row) + 8)
            matrix.append(key)
            keys.add(key)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            process_lpressed(chr(event.key))
            process_rpressed(chr(event.key))
        if event.type == pygame.KEYUP:
            process_lreleased(chr(event.key))
            process_rreleased(chr(event.key))
    app.fill(BG_COLOR)
    keys.draw(app)
    pygame.display.flip()
