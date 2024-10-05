import pygame
import settings as st
import math
import map as mp

class Player:
    def __init__(self):
        self.playerX = st.playerX
        self.playerY = st.playerY
        self.playerAngle = st.playerAngle
    def createPlayer(self, window, color, X, Y, size, angle):

        player_surface = pygame.Surface((size, size), pygame.SRCALPHA)
        player_surface.fill((0, 0, 0, 0))
        pygame.draw.rect(player_surface, color, (0, 0, size, size))

        rotated_surface = pygame.transform.rotate(player_surface, angle)
        
        new_rect = rotated_surface.get_rect(center=(X + size // 2, Y + size // 2))
        
        window.blit(rotated_surface, new_rect.topleft)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.playerX += st.playerSpeed * math.cos(self.playerAngle)
            self.playerY += st.playerSpeed * math.sin(self.playerAngle)
            if ((self.playerX // st.TILE) * st.TILE, (self.playerY // st.TILE) * st.TILE) in mp.world_map:
                self.playerX += -st.playerSpeed * math.cos(self.playerAngle)
                self.playerY += -st.playerSpeed * math.sin(self.playerAngle)
        if keys[pygame.K_s]:
            self.playerX += -st.playerSpeed * math.cos(self.playerAngle)
            self.playerY += -st.playerSpeed * math.sin(self.playerAngle)
            if ((self.playerX // st.TILE) * st.TILE, (self.playerY // st.TILE) * st.TILE) in mp.world_map:
                self.playerX += st.playerSpeed * math.cos(self.playerAngle)
                self.playerY += st.playerSpeed * math.sin(self.playerAngle)
            
        if keys[pygame.K_a]:
            self.playerAngle -= 0.02
        if keys[pygame.K_d]:
            self.playerAngle += 0.02