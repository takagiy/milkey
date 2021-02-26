import pygame
import sys
import os

KEY_SPRITE_SIZE = 256

APP_WIDTH = KEY_SPRITE_SIZE * 4 + 16
APP_HEIGHT = KEY_SPRITE_SIZE * 4 + 16
APP_SIZE = (APP_WIDTH, APP_HEIGHT)

BG_COLOR = (255, 255, 255)

pygame.init()
app = pygame.display.set_mode(APP_SIZE)

def quit():
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                quit()
    app.fill(BG_COLOR)
    pygame.display.flip()
