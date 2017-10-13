import pygame
import sys
import time
import random
import numpy as np
import os
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

H = 'hero'
X = 'wall'
E = 'enemy'
_ = 'empty'

map = np.array([  
  [X,X,X,X,X,X,X,X,X,X,X,X,X,X,X,X,X],
  [X,_,_,_,X,_,_,_,X,_,_,X,_,X,_,_,X],
  [X,_,H,_,X,_,_,_,X,_,_,X,_,X,_,_,X],
  [X,_,_,_,_,_,_,_,X,_,_,X,_,X,_,_,X],
  [X,_,_,_,_,_,_,_,X,_,_,X,_,X,_,_,X],
  [X,_,_,_,_,_,E,_,_,_,_,_,_,_,_,_,X],
  [X,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,X],
  [X,X,_,_,_,_,_,X,X,X,_,X,X,_,_,_,X],
  [X,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,X],
  [X,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,X],
  [X,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,X],
  [X,X,_,_,_,E,_,_,_,E,_,_,X,_,E,_,X],
  [X,_,_,_,_,_,X,_,_,_,_,_,X,_,_,_,X],
  [X,_,_,_,_,X,X,X,_,_,_,_,X,_,_,_,X],
  [X,X,X,X,X,X,X,X,X,X,X,X,X,X,X,X,X]])

rows = map.shape[0]
cols = map.shape[1]

GRIDSIZE = 20
GRID_WIDTH = SCREEN_WIDTH / GRIDSIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRIDSIZE

class Point(object):
    def __init__(self, type, position):
        self.type = type
        self.x = position[0]
        self.y = position[1]

    def move(self, direction):
      if direction == 'UP':
        self.y = self.y if self.y == 1 else self.y - 1
      elif direction == 'DOWN':
        self.y = self.y if self.y >= rows - 3 else self.y + 1
      elif direction == 'LEFT':
        self.x = self.x if self.x == 1 else self.x - 1
      elif direction == 'RIGHT':
        self.x = self.x if self.x >= cols - 3  else self.x + 1

    def draw(self, surf):
      print(os.getcwd())
      if self.type == 'wall':
        imagename = 'pygame/images/dick_warm_body.png'
      elif self.type == 'enemy':
        imagename = 'pygame/images/dick.png'
      elif self.type == 'hero':
        #imagename = 'pygame/images/dick_warm_head.png'
        imagename = 'pygame/images/mads.png'
      else:
       return
      image = pygame.image.load(imagename)
      imagerect = image.get_rect()
      surf.blit(image, (self.x * GRIDSIZE, self.y * GRIDSIZE))



if __name__ == '__main__':

  #draw map
  objects = []
  for y in range(0, rows):
    for x in range(0, cols):
      p = Point(map[y, x], (x,y));
      objects.append(p)
      if(map[y, x]=='hero'):
        hero = p;

  #catch Key press and move hero OBJECT (not image!!!) 
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == KEYDOWN:
        if event.key == K_UP:
          hero.move('UP')
        elif event.key == K_DOWN:
          hero.move('DOWN')
        elif event.key == K_LEFT:
          hero.move('LEFT')
        elif event.key == K_RIGHT:
          hero.move('RIGHT')

    #refresh HUD lol
    font = pygame.font.Font(None, 36)
    text = font.render('({},{}) ({},{})'.format(hero.x, hero.y, cols, rows), 1, (30, 30, 10))
    textpos = text.get_rect()
    textpos.centerx = 80
    surface.blit(text, textpos)
    
    #clear canvas
    screen.blit(surface, (0,0))
    surface.fill((255,255,255))

    #draw all my objects
    for obj in objects:
      obj.draw(surface)

    #update canvas
    pygame.display.flip()
    pygame.display.update()
