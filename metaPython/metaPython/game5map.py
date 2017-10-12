import pygame
import sys
import time
import random

from pygame.locals import *

FPS = 1
pygame.init()
fpsClock=pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()
surface.fill((255,255,255))
clock = pygame.time.Clock()

pygame.key.set_repeat(1, 40)

GRIDSIZE=20
GRID_WIDTH = SCREEN_WIDTH / GRIDSIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRIDSIZE
UP    = (0, -1)
DOWN  = (0, 1)
LEFT  = (-1, 0)
RIGHT = (1, 0)
    
screen.blit(surface, (0,0))


class Point(object):
    def __init__(self, height):
        self.position = (0,0)
        self.height = height
        self.randomize()

    def __init__(self, height, position):
        self.height = height
        self.position = (position[0]*GRIDSIZE, position[1]*GRIDSIZE)

    def randomize(self):
        self.position = (random.randint(0, GRID_WIDTH-1) * GRIDSIZE, random.randint(0, GRID_HEIGHT-1) * GRIDSIZE)

    def draw(self, surf):
        image = pygame.image.load('dick.png')
        imagerect = image.get_rect()
        surf.blit(image, (self.position[0], self.position[1]))
        pygame.display.flip()

if __name__ == '__main__':
  baseHeight = 0;

  surface.fill((255,255,255))
  for x in range(0, int(GRID_WIDTH-1)):
    for y in  range(0, int(GRID_HEIGHT-1)):
      k = random.randint(-10, 10)
      h = baseHeight

      Point(100, (x,y)).draw(surface)

  while True:    

    font = pygame.font.Font(None, 36)
    text = font.render('huy', 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = 20
    surface.blit(text, textpos)
    screen.blit(surface, (0,0))

    pygame.display.flip()
    pygame.display.update()
