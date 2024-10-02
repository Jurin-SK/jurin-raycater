import pygame
import settings as st
import map as mp
from player import *
import math
from raycasting import raycasting
from drawing import *

pygame.init()
screen = pygame.display.set_mode((st.width, st.height))
clock = pygame.time.Clock()
running = True

#playerX = st.playerX
#playerY = st.playerY
#playerAngle = st.playerAngle

drawing = Drawing()
player = Player()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))

    # Work here
    
    player.move()
    
    #pygame.draw.circle(screen, st.YELLOW, (playerX, playerY), st.playerSize)

    for x,y in mp.world_map:
        pygame.draw.rect(screen, st.WHITE, (x, y, st.TILE, st.TILE))
    
    drawing.background(screen)
    drawing.render3d(screen, player.playerX, player.playerY, player.playerAngle, drawing.textures)
    pygame.display.flip()

    clock.tick(st.fps)

pygame.quit()