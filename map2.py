import pygame
import settings as st

mapWidth = st.mapWidth - 1
mapHeight = st.mapHeight - 1

mapArray = st.mapArray

def generateMap(window, color):
    renderLinesCtrl = 0
    renderX = 0
    renderY = 0
    for mapByte in mapArray:
        if renderLinesCtrl > mapWidth:
            renderY += st.TILE
            renderX = 0
            renderLinesCtrl = 0

        if mapByte == 1:
            wall = pygame.draw.rect(window, color, (renderX, renderY, st.TILE, st.TILE))
        
        renderX += st.TILE
        renderLinesCtrl += 1
        
