import pygame
import math
import settings as st
from map import world_map

def mapping(a,b):
    return (a // st.TILE) * st.TILE, (b // st.TILE) * st.TILE
def raycasting(window, playerX, playerY, playerAngle):
    xm, ym = mapping(playerX, playerY)
    curAngle = playerAngle - st.HALF_FOV
    for ray in range(st.NUM_RAYS):
        sin_a = math.sin(curAngle)
        cos_a = math.cos(curAngle)

        # hard math D_; i didn´t understand
        x, dx = (xm + st.TILE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, st.width, st.TILE):
            depth_v = (x - playerX) / cos_a
            y = playerY + depth_v * sin_a
            if mapping(x + dx, y) in world_map:
                break
            x += dx * st.TILE
        
        y, dy = (ym + st.TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, st.height, st.TILE):
            depth_h = (y - playerY) / sin_a
            x = playerX + depth_h * cos_a
            if mapping(x, y + dy) in world_map:
                break
            y += dy * st.TILE

        depth =  depth_v if depth_v < depth_h else depth_h
        depth *= math.cos(playerAngle - curAngle)
        projHeight = st.POJCOEFF / (depth + 0.0001)
        c = 255 / (1 + depth * depth * 0.0001)
        color = (63 + c // 2, 63 + c // 2, 63 + c // 2)
        pygame.draw.rect(window, color, (ray * st.SCALE, st.height / 2 - projHeight // 2, st.SCALE, projHeight))
        curAngle += st.DELTA_ANGLE


