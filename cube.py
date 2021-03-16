import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

facciebuff = (
    (1, -1, -1),
    (1, 1, -1),
    (1, 1, 1),
    (1, -1, 1),  # Una faccia stop len 4
    (-1, -1, 1),
    (-1, 1, 1),  # Due faccie stop len 6
    (-1, 1, -1)

)

facciebordibuff = (
    (0, 1),
    (0, 3),
    (2, 3),
    (2, 1),  # Una faccia stop len 4
    (2, 5),
    (3, 4),
    (5, 4),  # Due faccie stop len 7 = 6 +1
    (5, 6),
    (6, 1)  # Tre faccie stop len 10
)

dentrofaccie = (
    (0, 3, 2, 1),
    (2, 3, 4, 5),
    (1, 2, 5, 6)
)

numface = {"una": 4, "due": 7, "tre": 10, "UNA": 0, "DUE": 1, "TRE": 2}
numarea = {"una": 4, "due": 6, "tre": 7}
coppiecolori = {"bianco": (1, 1, 1), "blu": (0, 0, 1), "rosso": (1, 0.2, 0.3), "arancione": (1, 0.5, 0.1),
                "verde": (0, 1, 0), "giallo": (1, 1, 0), "nero": (0, 0, 0)}

# Creo la faccia tipo

def faccie(scelta_nfaccie, face, translate, rotate, colore1="bianco", colore2="blu", colore3="bianco", colore_linea="nero"):

    # glTranslated(translate[0], translate[1], translate[2])
    # glRotated(rotate[0], rotate[1], rotate[2], rotate[3])
    #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # glMatrixMode(GL_MODELVIEW)
    # glLoadIdentity()
    #glTranslatef(0, 0, 1)

    glTranslated(translate[0], translate[1], translate[2])
    glRotated(rotate[0], rotate[1], rotate[2], rotate[3])

    glBegin(GL_QUADS)
    if face == "UNA":
        for vertice in dentrofaccie[numface.get(face)]:
            glColor3fv(coppiecolori.get(colore1))
            glVertex3fv(facciebuff[vertice])
    elif face == "DUE":
        for vertice in dentrofaccie[numface.get("UNA")]:
            glColor3fv(coppiecolori.get(colore1))
            glVertex3fv(facciebuff[vertice])
        for vertice in dentrofaccie[numface.get(face)]:
            glColor3fv(coppiecolori.get(colore2))
            glVertex3fv(facciebuff[vertice])
    elif face == "TRE":
        for vertice in dentrofaccie[numface.get("UNA")]:
            glColor3fv(coppiecolori.get(colore1))
            glVertex3fv(facciebuff[vertice])
        for vertice in dentrofaccie[numface.get("DUE")]:
            glColor3fv(coppiecolori.get(colore2))
            glVertex3fv(facciebuff[vertice])
        for vertice in dentrofaccie[numface.get(face)]:
            glColor3fv(coppiecolori.get(colore3))
            glVertex3fv(facciebuff[vertice])
    glEnd()

    glBegin(GL_LINES)
    count = 0
    for linee in facciebordibuff:
        if count < numface.get(scelta_nfaccie):
            for punto in linee:
                glColor3fv(coppiecolori.get(colore_linea))
                glVertex3fv(facciebuff[punto])
            count += 1
        else:
            break
    glEnd()

    glTranslated(-(translate[0]), -(translate[1]), -(translate[2]))
    glRotated(rotate[0], -(rotate[1]), -(rotate[2]), -(rotate[3]))

def on_start():
    # PRIMO STRATO
    #                    Translate  Rotate

    glPushMatrix()
    faccie("due", "DUE", [0, 0, 0], [90, 0, 0, 1], "verde", "bianco")
    glPopMatrix()
    # faccie("tre", "TRE", [2, 0, 0], [0, 0, 0, 0], "arancione", "bianco", "verde")
    #
    # faccie("due", "DUE", [2, 0, -2], [90, -1, 0, 0], "arancione", "verde")
    #
    # faccie("tre", "TRE", [2, -2, -2], [90, -1, 0, 0], "arancione", "verde", "giallo")

    # faccie("tre", "TRE", [0, 4, 0], [90, 0, 0, 0], "bianco", "rosso", "verde")
    #
    # faccie("due", "DUE", [0, 4, -2], [90, -1, 0, 0], "bianco", "verde")
    #
    # faccie("tre", "TRE", [0, -2, -6], [90, -1, 0, 0], "bianco", "verde", "arancione")
    #
    # faccie("tre", "TRE", [0, -10, 2], [180, 1, 0, 0], "bianco", "arancione", "blu")
    #
    # faccie("due", "DUE", [0, 0, 2], [180, 1, 0, 0], "bianco", "arancione")

    # # SECONDO STRATO
    #
    # glTranslated(-2, 0, 0)
    # glRotated(90, 0, 0, 1)
    # faccie("due", "DUE", "blu", "arancione")
    #
    # glTranslated(0, 0, -2)
    # glRotated(90, 0, 0, 0)
    # faccie("una", "UNA", "blu")
    #
    # glTranslated(0, 0, -2)
    # glRotated(90, 0, 1, 0)
    # faccie("due", "DUE", "rosso", "blu")
    #
    # glTranslated(0, 0, -2)
    # glRotated(90, 0, 0, 0)
    # faccie("una", "UNA", "rosso")
    #
    # glTranslated(0, 0, -2)
    # glRotated(90, 0, 1, 0)
    # faccie("due", "DUE", "verde", "rosso")
    #
    # glTranslated(0, 0, -2)
    # glRotated(90, 0, 0, 0)
    # faccie("una", "UNA", "verde")
    #
    # glTranslated(0, 0, -2)
    # glRotated(90, 0, 1, 0)
    # faccie("due", "DUE", "arancione", "verde")
    #
    # glTranslated(0, 0, -2)
    # glRotated(90, 0, 0, 0)
    # faccie("una", "UNA", "arancione")
    #
    # # TERZO STRATO
    #
    # glTranslated(0, 2, 0)
    # glRotated(90, -1, 0, 0)
    # faccie("due", "DUE", "arancione", "giallo")
    #
    # glTranslated(0, 2, 0)
    # glRotated(90, 0, 0, 0)
    # faccie("tre", "TRE", "arancione", "giallo", "blu")
    #
    # glTranslated(-2, 0, 0)
    # glRotated(90, 0, 0, 1)
    # faccie("due", "DUE", "blu", "giallo")
    #
    # glTranslated(0, 2, 0)
    # glRotated(90, 0, 0, 0)
    # faccie("tre", "TRE", "blu", "giallo", "rosso")
    #
    # glTranslated(-2, 0, 0)
    # glRotated(90, 0, 0, 1)
    # faccie("due", "DUE", "rosso", "giallo")
    #
    # glTranslated(0, 2, 0)
    # glRotated(90, 0, 0, 0)
    # faccie("tre", "TRE", "rosso", "giallo", "verde")
    #
    # glTranslated(-2, 0, 0)
    # glRotated(90, 0, 0, 1)
    # faccie("due", "DUE", "verde", "giallo")
    #
    # glTranslated(0, 2, 0)
    # glRotated(90, 0, 0, 0)
    # faccie("tre", "TRE", "verde", "giallo", "arancione")
    #
    # glTranslated(-2, -2, 0)
    # glRotated(90, 0, -1, 0)
    # faccie("una", "UNA", "giallo")


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(-1.0, 1.0, -25)  # Camera view
    glRotatef(45, 1, 1, 1)  # Prospective view

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    #Impedisco l'overlapping
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    #Creo il cubo
    on_start()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:  # F'
                    glRotatef(45, 0, 0, 1)
                if event.key == pygame.K_f:  # F
                    glRotate(45, 0, 0, -1)
                if event.key == pygame.K_y:  # U'
                    glRotatef(90, 1, 0, 0)
                if event.key == pygame.K_u:  # U
                    glRotatef(90, -1, 0, 0)
                if event.key == pygame.K_t:  # R'
                    glRotatef(90, 0, -1, 0)
                if event.key == pygame.K_r:  # R
                    glRotatef(90, 0, 1, 0)
                if event.key == pygame.K_k:  # L'
                    glRotatef(1, 0, 2, 1)
                if event.key == pygame.K_l:  # L
                    glRotatef(90, 1, 0, 0)
                if event.key == pygame.K_s:  # D'
                    glRotatef(1, 0, 2, 1)
                if event.key == pygame.K_d:  # D
                    glRotatef(90, 1, 0, 0)

        #glRotatef(90, -1, -1, 1)
        pygame.display.flip()
        pygame.time.wait(10)
    glDisable(GL_DEPTH_TEST)
if __name__ == '__main__':
    main()
