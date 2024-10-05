import pygame
import settings as st
import raycasting as ry

class Drawing:

    def __init__(self):
        self.textures = {
            "1": pygame.image.load('textures/brick.png').convert(),
            "2": pygame.image.load('textures/brick2.png').convert(),
            "3": pygame.image.load('textures/brick3.png').convert(),
            "4": pygame.image.load('textures/danger.png').convert(),
            "5": pygame.image.load('textures/metal.png').convert(),
            "6": pygame.image.load('textures/metal2.png').convert()
        }

    def background(self, window):
        pygame.draw.rect(window, st.GRAY, (0, 0, st.width, st.width / 2))
        pygame.draw.rect(window, st.RED, (0, st.height / 2, st.width, st.height / 2))
    def render3d(self, window, playerX, playerY, playerAngle, textures):
        ry.raycasting(window, playerX, playerY, playerAngle, textures)