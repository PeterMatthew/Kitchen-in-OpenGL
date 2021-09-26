from OpenGL.GL import *

def create_block(x, y, z, width, height, depth, **kwargs):
  side = { 'leftTexture', 'rightTexture', 'frontTexture', 'backTexture', 'topTexture',
           'bottomTexture', 'restTexture' }

  if 'restTexture' in kwargs:
    rest = set(side) - set(kwargs)
    for each in rest:
      kwargs[each] = kwargs['restTexture']

  glEnable(GL_TEXTURE_2D)
  glBindTexture(GL_TEXTURE_2D, kwargs['frontTexture'])

  glBegin(GL_QUADS)
  glNormal3f(0, 0, 1)
  glTexCoord2f(0.0, 0.0)
  glVertex3f(x, y, z)
  glTexCoord2f(1.0, 0.0)
  glVertex3f(x+width, y, z)
  glTexCoord2f(1.0, 1.0)
  glVertex3f(x+width, y+height, z)
  glTexCoord2f(0.0, 1.0)
  glVertex3f(x, y+height, z)
  glEnd()

  glDisable(GL_TEXTURE_2D)

  glEnable(GL_TEXTURE_2D)
  glBindTexture(GL_TEXTURE_2D, kwargs['backTexture'])

  glBegin(GL_QUADS)
  glNormal3f(0, 0, -1)
  glTexCoord2f(0.0, 0.0)
  glVertex3f(x, y, z-depth)
  glTexCoord2f(1.0, 0.0)
  glVertex3f(x+width, y, z-depth)
  glTexCoord2f(1.0, 1.0)
  glVertex3f(x+width, y+height, z-depth)
  glTexCoord2f(0.0, 1.0)
  glVertex3f(x, y+height, z-depth)
  glEnd()

  glDisable(GL_TEXTURE_2D)

  glEnable(GL_TEXTURE_2D)
  glBindTexture(GL_TEXTURE_2D, kwargs['leftTexture'])

  glBegin(GL_QUADS)
  glNormal3f(-1, 0, 0)
  glTexCoord2f(0.0, 0.0)
  glVertex3f(x, y, z)
  glTexCoord2f(1.0, 0.0)
  glVertex3f(x, y, z-depth)
  glTexCoord2f(1.0, 1.0)
  glVertex3f(x, y+height, z-depth)
  glTexCoord2f(0.0, 1.0)
  glVertex3f(x, y+height, z)
  glEnd()

  glDisable(GL_TEXTURE_2D)

  glEnable(GL_TEXTURE_2D)
  glBindTexture(GL_TEXTURE_2D, kwargs['rightTexture'])

  glBegin(GL_QUADS)
  glNormal3f(1, 0, 0)
  glTexCoord2f(0.0, 0.0)
  glVertex3f(x+width, y, z)
  glTexCoord2f(1.0, 0.0)
  glVertex3f(x+width, y, z-depth)
  glTexCoord2f(1.0, 1.0)
  glVertex3f(x+width, y+height, z-depth)
  glTexCoord2f(0.0, 1.0)
  glVertex3f(x+width, y+height, z)
  glEnd()

  glDisable(GL_TEXTURE_2D)

  glEnable(GL_TEXTURE_2D)
  glBindTexture(GL_TEXTURE_2D, kwargs['topTexture'])

  glBegin(GL_QUADS)
  glNormal3f(0, -1, 0)
  glTexCoord2f(0.0, 0.0)
  glVertex3f(x, y+height, z)
  glTexCoord2f(1.0, 0.0)
  glVertex3f(x, y+height, z-depth)
  glTexCoord2f(1.0, 1.0)
  glVertex3f(x+width, y+height, z-depth)
  glTexCoord2f(0.0, 1.0)
  glVertex3f(x+width, y+height, z)
  glEnd()

  glDisable(GL_TEXTURE_2D)

  glEnable(GL_TEXTURE_2D)
  glBindTexture(GL_TEXTURE_2D, kwargs['bottomTexture'])

  glBegin(GL_QUADS)
  glNormal3f(0, -1, 0)
  glTexCoord2f(0.0, 0.0)
  glVertex3f(x, y, z)
  glTexCoord2f(1.0, 0.0)
  glVertex3f(x, y, z-depth)
  glTexCoord2f(1.0, 1.0)
  glVertex3f(x+width, y, z-depth)
  glTexCoord2f(0.0, 1.0)
  glVertex3f(x+width, y, z)
  glEnd()

  glDisable(GL_TEXTURE_2D)