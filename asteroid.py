import circleshape
import pygame
import constants
import random

class Asteroid(circleshape.CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()

    if self.radius == constants.ASTEROID_MIN_RADIUS:
      return
    
    angle = random.uniform(20, 50)
    p = self.velocity.rotate(angle)
    n = self.velocity.rotate(-angle)

    r = self.radius - constants.ASTEROID_MIN_RADIUS

    a1 = Asteroid(self.position.x, self.position.y, r)
    a2 = Asteroid(self.position.x, self.position.y, r)

    a1.velocity = p * 1.2
    a2.velocity = n * 1.2