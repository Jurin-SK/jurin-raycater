from settings import *

text_map = [
    '111166666111',
    '1..........1',
    '1..22......1',
    '1..1...1...1',
    '1..1.......1',
    '1..1111....1',
    '1.......1..1',
    '111111111111'
]

world_map = {}
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != ".":
            if char == '1': world_map[(i * TILE, j * TILE)] = '1'
            elif char == '2': world_map[(i * TILE, j * TILE)] = '2'  
            elif char == '6': world_map[(i * TILE, j * TILE)] = '6'       
