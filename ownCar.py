from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def myint():
    glMatrixMode(GL_PROJECTION)
    #glOrtho(-10,10,-10,10,-10,10)
    gluPerspective(60,1,0.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)
    glClearColor(1,1,1,1)


x=0
angle=0
r=.1
z=1.5
s=True

def draw():

        global  x
        global angle
        global r
        global z
        global s
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1, 0, 0)


        #Body
        glLoadIdentity()
        glTranslate(x, 0, 0)
        glScale(1,.25,.5)
        glutWireCube(5)


        #Head
        glLoadIdentity()
        glTranslate(x+0,5*.25,0)
        glScale(.5,.25,.5)
        glutWireCube(5)


        #backbody
        glLoadIdentity()
        glTranslate(-3+x,5*.25,0)
        glScale(.5,.5,.5)
        glutWireCube(9)



        #Tires
        #L.F
        glLoadIdentity()
        glTranslate(x+5*.5,-.5,-5*.25)
        glRotate(angle,0,0,1)
        glutWireTorus(0.125, 0.5, 20, 10)

        #R.Forward
        glLoadIdentity()
        glTranslate(x+5 * .5, -.5, 5 * .25)
        glRotate(angle,0,0,1)
        glutWireTorus(0.125, 0.5, 20, 10)

        # L.Back
        glLoadIdentity()
        glTranslate(x+ -5 * .5, -.5, -5 * .25)
        glRotate(angle,0,0,1)
        glutWireTorus(0.125, 0.5, 20, 10)

        # R.B
        glLoadIdentity()
        glTranslate(-5 * .5 + x, -.5, 5 * .25)
        glRotate(angle,0,0,1)
        glutWireTorus(0.125, 0.5, 20, 10)



        #L.light
        glLoadIdentity()
        glColor(0,1,s)
        glTranslate(5*.5+x,0,-.5)
        glutWireSphere(0.25, 100, 100)

        # F.light
        glLoadIdentity()
        glColor(0, 1, s)
        glTranslate(5 * .5+x, 0, .5)
        glutWireSphere(0.25, 100, 100)



        x=x+r
        angle=angle-z
        s=not s
        glFlush()

        if(x>=10 or x<=-10):
         r=-r
         z=-z











glutInit()
# initialize variables of opengl

glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

#Buffer Mode:
#Single ==> show drawing step by step"""

glutInitWindowSize(600,600)
# External windows size

glutCreateWindow(b"wall-E")
# create window and set it's name

glutDisplayFunc(draw)
# take the drawing function and call it when event is called
glutIdleFunc(draw)
myint()

glutMainLoop()
# redraw the graphic, loop over all the program

