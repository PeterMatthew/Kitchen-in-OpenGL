from OpenGL.GL import *
from OpenGL.GLU import *
import glm

class Camera:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.pos = glm.vec3(17, 5, 10)
    self.front = glm.vec3(0, 0, -1)
    self.up = glm.vec3(0, 1, 0)
    self.speed = 0.5

  def init(self):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(75, self.width/self.height, 0.1, 600)

  def update(self):
    new = self.pos + self.front
    gluLookAt(self.pos.x, self.pos.y, self.pos.z, new.x, new.y, new.z, 0, 1, 0)

  def goFoward(self):
    self.pos += self.speed * self.front

  def goBackward(self):
    self.pos -= self.speed * self.front

  def goLeft(self):
    self.pos -= glm.normalize(glm.cross(self.front, self.up)) * self.speed

  def goRight(self):
    self.pos += glm.normalize(glm.cross(self.front, self.up)) * self.speed