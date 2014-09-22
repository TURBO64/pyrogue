#!/usr/bin/python3

import random

from game import *
from console import *
from tile import *
from world import *
from creature import *

# ---- map functions ----
def draw_map():
  for x, col in enumerate(current_map.grid):
    for y, cell in enumerate(col):
      if cell.color > 6:
        cons.setbold()
      cons.setcolor(cell.color)
      cons.putchar(y, x, cell.char)
      cons.unsetcolor(cell.color)
      cons.unsetbold()

def flood(tile):
  current_map.grid = [[ tile
    for y in range(current_map.height) ]
      for x in range(current_map.width) ]

def addtile(tile, x, y):
  current_map.grid[x][y] = tile

def spray(tile, n):
  for x in range(n):
    rx = random.randint(0, current_map.width - 1)
    ry = random.randint(0, current_map.height - 1)
    addtile(tile, rx, ry)

def rect(tile, startx, starty, width, height):
  for x in range(startx, startx + width):
    for y in range(starty, starty + height):
      addtile(tile, x, y)

def room(startx, starty, width, height):
  rect(tile_grass, startx - 1, starty - 1, width + 3, height + 3) # make accessible
  rect(tile_floor, startx, starty, width, height)                 # floor
  rect(tile_wall, startx, starty, width, 1)                       # top
  rect(tile_wall, startx, starty + height, width + 1, 1)          # bottom
  rect(tile_wall, startx, starty, 1, height)                      # left
  rect(tile_wall, startx + width, starty, 1, height)              # right
  addtile(tile_door, startx + int(width / 2), starty + height)    # door

# ---- end map functions ----


# ---- player functions ----
def draw_player():
  if player.x in range(current_map.width):
    if player.y in range(current_map.height):
      if player.color > 6:
        cons.setbold()
      cons.setcolor(player.color)
      cons.putchar(player.y, player.x, player.char)
      cons.unsetcolor(player.color)
      cons.unsetbold()
      
def move_player(dx, dy):
  newx = player.x + dx
  newy = player.y + dy
  if newx in range(current_map.width):
    if newy in range(current_map.height):
      if current_map.getchar(newx, newy) == '.':
        player.x = newx
        player.y = newy
        # move action successful
        return 0
  else:
    # move action failed
    return 1
    
def get_input():
  key = getch()
  if   key == ord('q'):         # quit
    game.end = True
  elif key is ord('h'):         # left
    if move_player(-1, 0) == 0:
      game.turn += 1
  elif key is ord('j'):         # down
    if move_player(0, 1) == 0:
      game.turn += 1
  elif key is ord('k'):         # up
    if move_player(0, -1) == 0:
      game.turn += 1
  elif key is ord('l'):         # right
    if move_player(1, 0) == 0:
      game.turn += 1
      
# ---- end player functions ----
      
      
# ---- game start ----
 
cons = Console()
game = Game()
current_map = World()

tile_grass = Tile('grass', '.', 3)
tile_dirt  = Tile('dirt',  '.', 2)
tile_tree  = Tile('tree',  'Y', 2)
tile_floor = Tile('floor', '.', 0)
tile_wall  = Tile('wall',  '#', 0)
tile_door  = Tile('door',  '+', 2)

player = Creature('player', '@', 4)
player.x = 15
player.y = 10

flood(tile_grass)
spray(tile_tree, 16)
spray(tile_dirt, 64)
room(12, 4, 7, 4)


# begin main loop
while game.end == False:
  # clear the screen
  cons.clear()
  # render everything
  draw_map()
  draw_player()
  
  # debug stuff
  move(0, 41)
  addstr("Turns: " + str(game.turn) )
  move(1, 41)
  addstr("Player X: " + str(player.x) )
  move(2, 41)
  addstr("Player Y: " + str(player.y) )
  
  # handle input
  get_input()

# end main loop

# close window
cons.close()
