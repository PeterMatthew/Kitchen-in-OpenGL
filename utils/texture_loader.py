from OpenGL.GL import *
import pygame

def load_texture(path):
  texture_data = pygame.image.load(path)
  width = texture_data.get_width()
  height = texture_data.get_height()
  texture_data = pygame.image.tostring(texture_data, 'RGBA', 1)

  texture = glGenTextures(1)
  glBindTexture(GL_TEXTURE_2D, texture)
  glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT) 
  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

  glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)

  glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
  glGenerateMipmap(GL_TEXTURE_2D)
  return texture