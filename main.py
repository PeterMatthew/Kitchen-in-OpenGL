from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import glm
from utils.camera import Camera
from utils.texture_loader import load_texture
from utils.block_creator import create_block

textures = {}

WIDTH, HEIGHT = 800, 600

pastX = WIDTH/2
pastY = HEIGHT/2
angleX = -90
angleY = 0

t = 0
doorOpen = False

cam = Camera(WIDTH, HEIGHT)

def keyboard(key, x, y):
  if key == b'w':
    cam.goFoward()
  elif key == b's':
    cam.goBackward()
  elif key == b'a':
    cam.goLeft()
  elif key == b'd':
    cam.goRight()
  elif key == b'p':
    global doorOpen
    if doorOpen:
      doorOpen = False
    else:
      doorOpen = True


def mouse(x, y):
  global pastX, pastY, angleX, angleY

  changeX = (x - pastX) * 0.4
  changeY = (y - pastY) * 0.4

  angleX += changeX
  angleY += changeY

  if angleY > 89:
    angleY = 89
  if angleY < -89:
    angleY = -89

  direction = glm.vec3()

  direction.y = glm.sin(glm.radians(angleY))
  direction.x = glm.cos(glm.radians(angleY)) * glm.cos(glm.radians(angleX))
  direction.z = glm.cos(glm.radians(angleY)) * glm.sin(glm.radians(angleX))

  cam.front = glm.normalize(direction)

  pastX = x
  pastY = y


def draw_room():
  create_block(0, 0, 0, 15, 10, 1, restTexture=textures['brick'], backTexture=textures['wall'])
  create_block(20, 0, 0, 15, 10, 1, restTexture=textures['brick'], backTexture=textures['wall'])
  if doorOpen:
    glPushMatrix()
    glTranslatef(15, 0, 0)
    glRotatef(75, 0, 1, 0)
    create_block(0, 0, 0, 5, 10, 1, restTexture=textures['wood'], backTexture=textures['door'], frontTexture=textures['door'])
    glPopMatrix()
  else:
    create_block(15, 0, 0, 5, 10, 1, restTexture=textures['wood'], backTexture=textures['door'], frontTexture=textures['door'])

  create_block(-1, 0, 0, 1, 10, 30, restTexture=textures['brick'], rightTexture=textures['wall'])
  create_block(35, 0, 0, 1, 10, 30, restTexture=textures['brick'], leftTexture=textures['wall'])

  create_block(0, 0, -30, 35, 10, 1, restTexture=textures['brick'], frontTexture=textures['wall'])

  create_block(0, 0, 0, 35, 0, 30, restTexture=textures['floor'])
  create_block(0, 10, 0, 35, 0, 30, restTexture=textures['wall'])

def draw_picture():
  create_block(0.1, 4, -15, 0, 4, 3, restTexture=textures['picture'])
  create_block(0.1, 3.7, -15, 0.2, 0.3, 3, restTexture=textures['floor'])
  create_block(0.1, 8, -15, 0.2, 0.3, 3, restTexture=textures['floor'])
  create_block(0.1, 3.7, -14.7, 0.2, 4.6, 0.3, restTexture=textures['floor'])
  create_block(0.1, 3.7, -18, 0.2, 4.6, 0.3, restTexture=textures['floor'])

def draw_table():
  create_block(13, 3, -10, 9, 0.5, 7, restTexture=textures['wood'])
  create_block(13.5, 0, -10.5, 0.5, 3, 0.5, restTexture=textures['wood'])
  create_block(13.5, 0, -16, 0.5, 3, 0.5, restTexture=textures['wood'])
  create_block(21, 0, -10.5, 0.5, 3, 0.5, restTexture=textures['wood'])
  create_block(21, 0, -16, 0.5, 3, 0.5, restTexture=textures['wood'])

def draw_chair():
  create_block(15, 1.5, -18, 2, 0.5, 2, restTexture=textures['wood'])
  create_block(15, 1.5, -20, 2, 3, 0.3, restTexture=textures['wood'])
  create_block(15, 0, -18, 0.3, 1.5, 0.3, restTexture=textures['wood'])
  create_block(16.7, 0, -18, 0.3, 1.5, 0.3, restTexture=textures['wood'])
  create_block(15, 0, -20, 0.3, 1.5, 0.3, restTexture=textures['wood'])
  create_block(16.7, 0, -20, 0.3, 1.5, 0.3, restTexture=textures['wood'])

def draw_fridge():
  create_block(25, 0, -26.5, 5, 8.5, 2, frontTexture=textures['fridge'], restTexture=textures['fridge2'])

def draw_cabinet():
  create_block(10, 3, -27, 7, 0.5, 3, restTexture=textures['marble'])
  create_block(10.5, 0, -27.5, 6, 3, 2.5, restTexture=textures['wood'])
  create_block(10.7, 0.2, -27.3, 2.7, 2.6, 0.2, restTexture=textures['wood'])
  create_block(13.6, 0.2, -27.3, 2.7, 2.6, 0.2, restTexture=textures['wood'])
  create_block(13.2, 0.2, -27.1, 0.2, 2.6, 0.2, restTexture=textures['metal'])
  create_block(13.6, 0.2, -27.1, 0.2, 2.6, 0.2, restTexture=textures['metal'])

  create_block(10.5, 5, -27.5, 6, 5, 2.5, restTexture=textures['wood'])
  create_block(10.7, 5.2, -27.3, 2.7, 4.6, 0.2, restTexture=textures['wood'])
  create_block(13.6, 5.2, -27.3, 2.7, 4.6, 0.2, restTexture=textures['wood'])
  create_block(13.6, 5.2, -27.1, 2.7, 0.2, 0.2, restTexture=textures['metal'])
  create_block(10.7, 5.2, -27.1, 2.7, 0.2, 0.2, restTexture=textures['metal'])

def draw_fan():
  create_block(16.75, 8.5, -14.75, 0.5, 1.5, 0.5, restTexture=textures['metal'])
  global t
  t += 1
  if t > 359: t = 0
  glPushMatrix()
  glTranslatef(17, 8.5, -15)
  glRotatef(t, 0, -1, 0)
  create_block(0, 0, 0.5, 5, 0.1, 1, restTexture=textures['metal'])
  create_block(0, 0, 0.5, -5, 0.1, 1, restTexture=textures['metal'])
  create_block(-0.5, 0, 0, 1, 0.1, 5, restTexture=textures['metal'])
  create_block(-0.5, 0, 0, 1, 0.1, -5, restTexture=textures['metal'])
  glPopMatrix()


def showScreen():
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()

  cam.update()
  
  glLightfv(GL_LIGHT0, GL_POSITION, [17, 4, -14, 1])
  glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [0, 1, 0])
  glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 90)

  draw_room()
  draw_table()
  draw_chair()
  draw_picture()
  draw_fridge()
  draw_cabinet()
  draw_fan()

  glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowSize(WIDTH, HEIGHT)
glutInitWindowPosition(0, 0)
glutCreateWindow("window")

textures['brick'] = load_texture('textures/brick.jpg')
textures['wall'] = load_texture('textures/wall.jpg')
textures['door'] = load_texture('textures/door.jpg')
textures['floor'] = load_texture('textures/floor.jpg')
textures['picture'] = load_texture('textures/picture.jpg')
textures['wood'] = load_texture('textures/wood.jpg')
textures['metal'] = load_texture('textures/metal.jpg')
textures['marble'] = load_texture('textures/marble.jpg')
textures['fridge'] = load_texture('textures/fridge.png')
textures['fridge2'] = load_texture('textures/fridge2.png')

glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutKeyboardFunc(keyboard)
glutPassiveMotionFunc(mouse)

glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 1, 1])
glLightfv(GL_LIGHT0, GL_SPECULAR, [1, 1, 1, 1])
glEnable(GL_COLOR_MATERIAL)
glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.5, 0.5, 0.5, 1])

cam.init()

glutMainLoop()

