import pygame
from constants import *
import player
import asteroid
import asteroidfield
import sys
import shot

def main():
  print('Starting asteroids!')
  print(f'Screen width: {SCREEN_WIDTH}')
  print(f'Screen height: {SCREEN_HEIGHT}')
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  player.Player.containers = (updatable, drawable)
  asteroids = pygame.sprite.Group()
  asteroid.Asteroid.containers = (asteroids, updatable, drawable)
  asteroidFields = pygame.sprite.Group()
  asteroidfield.AsteroidField.containers = (updatable)
  asteroidField = asteroidfield.AsteroidField()
  shots = pygame.sprite.Group()
  shot.Shot.containers = (shots, updatable, drawable)
  p = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
    screen.fill((0,0,0))
    for u in updatable:
      u.update(dt)

    for a in asteroids:
      if a.collide(p):
        print('Game over!')
        sys.exit()

    for s in shots:
      for a in asteroids:
        if s.collide(a):
          s.kill()
          a.split()

    for d in drawable:
      d.draw(screen)
    pygame.display.flip()
    delta = clock.tick(120)
    dt = delta / 1000

if __name__ == "__main__":
  main()