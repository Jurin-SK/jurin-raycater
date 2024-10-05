import pygame
import math
import settings as st
from map import world_map

def mapping(a,b):
    return (a // st.TILE) * st.TILE, (b // st.TILE) * st.TILE
def raycasting(window, playerX, playerY, playerAngle, textures):
    xm, ym = mapping(playerX, playerY)
    curAngle = playerAngle - st.HALF_FOV
    for ray in range(st.NUM_RAYS):
        sin_a = math.sin(curAngle)
        cos_a = math.cos(curAngle)

        # hard math D_; i didn´t understand
        xd, dx = (xm + st.TILE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, st.width, st.TILE):
            depth_v = (xd - playerX) / cos_a
            y = playerY + depth_v * sin_a
            tile_v = mapping(xd + dx, y)
            if tile_v in world_map:
                texture_v = world_map[tile_v]
                break
            xd += dx * st.TILE
        
        yd, dy = (ym + st.TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, st.height, st.TILE):
            depth_h = (yd - playerY) / sin_a
            x = playerX + depth_h * cos_a
            tile_h = mapping(x, yd + dy)
            if tile_h in world_map:
                texture_h = world_map[tile_h]
                break
            yd += dy * st.TILE
        
        depth, offset, texture = (depth_v, y, texture_v) if depth_v < depth_h else (depth_h, x, texture_h)
        offset = int(offset) % st.TILE
        depth *= math.cos(playerAngle - curAngle)
        depth = max(depth, 0.00001)
        projHeight = min(int(st.POJCOEFF / depth), 2 * st.height)
        wallColumn = textures[texture].subsurface(offset * st.TEXTURE_SCALE, 0, st.TEXTURE_SCALE, st.TEXTURE_HEIGHT)
        wallColumn = pygame.transform.scale(wallColumn, (st.SCALE, projHeight))
        window.blit(wallColumn, (ray * st.SCALE, st.height // 2 - projHeight // 2))
        curAngle += st.DELTA_ANGLE
        # depth =  depth_v if depth_v < depth_h else depth_h
        # depth *= math.cos(playerAngle - curAngle)
        # projHeight = st.POJCOEFF / (depth + 0.0001)
        # c = 255 / (1 + depth * depth * 0.0001)
        # color = (63 + c // 2, 63 + c // 2, 63 + c // 2)
        # pygame.draw.rect(window, color, (ray * st.SCALE, st.height / 2 - projHeight // 2, st.SCALE, projHeight))
        # curAngle += st.DELTA_ANGLE


