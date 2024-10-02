import pygame
import sys

# Inicializácia Pygame
pygame.init()

# Nastavenie okna
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Načítanie textúry podlahy
floor_texture = pygame.image.load('textures/brick.png')
floor_rect = floor_texture.get_rect(topleft=(0, HEIGHT - 50))  # Podlaha 50 pixelov odspodu

# Hlavný herný cyklus
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Získaj pozíciu hráča (napr. myš alebo iný objekt)
    player_x, player_y = pygame.mouse.get_pos()
    player_y += 50  # Simuluj výšku hráča

    # Raycasting (zjednodušené)
    if player_y >= HEIGHT - 50:  # Hráč narazí na podlahu
        # Vykresli podlahu
        screen.blit(floor_texture, floor_rect)

    # Obnov obrazovku
    pygame.display.flip()
    screen.fill((0, 0, 0))  # Vymaž obrazovku
