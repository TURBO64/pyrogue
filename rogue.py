#!/usr/bin/python3

import curses
import random

# wrapper handles curses subroutines to
# prevent console borking from crashes

# constants
map_width = 40
map_height = 16
win_main = curses.initscr()

# classes
class Game:
  def __init__(self):
    self.over = False
    self.turn = 0

class Interface:
  def __init__(self):
    curses.noecho()
    curses.cbreak()
    curses.curs_set(False)
    win_main.keypad(True)
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair( 0, curses.COLOR_WHITE,   curses.COLOR_BLACK)
    curses.init_pair( 1, curses.COLOR_RED,     curses.COLOR_BLACK)
    curses.init_pair( 2, curses.COLOR_YELLOW,  curses.COLOR_BLACK)
    curses.init_pair( 3, curses.COLOR_GREEN,   curses.COLOR_BLACK)
    curses.init_pair( 4, curses.COLOR_CYAN,    curses.COLOR_BLACK)
    curses.init_pair( 5, curses.COLOR_BLUE,    curses.COLOR_BLACK)
    curses.init_pair( 6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair( 7, curses.COLOR_WHITE,   curses.COLOR_BLACK)
    curses.init_pair( 8, curses.COLOR_RED,     curses.COLOR_BLACK)
    curses.init_pair( 9, curses.COLOR_YELLOW,  curses.COLOR_BLACK)
    curses.init_pair(10, curses.COLOR_GREEN,   curses.COLOR_BLACK)
    curses.init_pair(11, curses.COLOR_CYAN,    curses.COLOR_BLACK)
    curses.init_pair(12, curses.COLOR_BLUE,    curses.COLOR_BLACK)
    curses.init_pair(13, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
  def close(self):
    curses.nocbreak()
    curses.echo()
    win_main.keypad(False)
    curses.endwin()
  def clear(self):
    win_main.clear()
  def putchar(self, y, x, char):
    win_main.move(y, x)
    win_main.addch(char)
  def setcolor(self, n):
    win_main.attron(curses.color_pair(n) )
  def unsetcolor(self, n):
    win_main.attroff(curses.color_pair(n) )
  def setbold(self):
    win_main.attron(curses.A_BOLD)
  def unsetbold(self):
    win_main.attroff(curses.A_BOLD)
  def getinput(self):
    key = win_main.getkey()
    if key == 'q':
      game.over = True
    elif key == 'h':
      if player.move(-1, 0) == 0:
        game.turn += 1
    elif key == 'j':
      if player.move(0, 1) == 0:
        game.turn += 1
    elif key == 'k':
      if player.move(0, -1) == 0:
        game.turn += 1
    elif key == 'l':
      if player.move(1, 0) == 0:
        game.turn += 1

class Tile:
  def __init__(self, name, char, color):
    self.name  = name
    self.char  = char
    self.color = color

class Map:
  # init map with grass
  def __init__(self):
    self.grid = [[ tile_grass
      for y in range(map_height) ]
        for x in range(map_width) ]
  # return char from tile
  def getchar(self, y, x):
    return self.grid[y][x].char
  # render the map
  def draw(self):
    for x, col in enumerate(self.grid):
      for y, cell in enumerate(col):
        if cell.color > 6:
          io.setbold()
        io.setcolor(cell.color)
        io.putchar(y, x, cell.char)
        io.unsetcolor(cell.color)
        io.unsetbold()
  # add a single tile
  def add(self, tile, x, y):
    self.grid[x][y] = tile
  # random spray of tiles
  def spray(self, tile, n):
    for x in range(n):
      rx = random.randint(0, map_width - 1)
      ry = random.randint(0, map_height - 1)
      self.add(tile, rx, ry)
  # filled rectangle
  def rect(self, tile, startx, starty, width, height):
    for x in range(startx, startx + width):
      for y in range(starty, starty + height):
        self.add(tile, x, y)
  # room with a door
  def room(self, startx, starty, width, height):
    self.rect(tile_grass, startx - 1, starty - 1, width + 3, height + 3) # make accessible
    self.rect(tile_floor, startx, starty, width, height)                 # floor
    self.rect(tile_wall, startx, starty, width, 1)                       # top
    self.rect(tile_wall, startx, starty + height, width + 1, 1)          # bottom
    self.rect(tile_wall, startx, starty, 1, height)                      # left
    self.rect(tile_wall, startx + width, starty, 1, height)              # right
    self.add(tile_door, startx + int(width / 2), starty + height)        # door

class Creature:
  def __init__(self, name, char, color):
    self.name  = name
    self.char  = char
    self.color = color
    self.x, self.y = -1, -1
  def draw(self):
    if self.x in range(map_width):
      if self.y in range(map_height):
        if self.color > 6:
          io.setbold()
        io.setcolor(self.color)
        io.putchar(self.y, self.x, self.char)
        io.unsetcolor(self.color)
        io.unsetbold()
  def move(self, dx, dy):
    newx = self.x + dx
    newy = self.y + dy
    if newx in range(map_width):
      if newy in range(map_height):
        if current_map.getchar(newx, newy) == '.':
          self.x = newx
          self.y = newy
          # move action successful
          return 0
    else:
      # move action failed
      return 1
 
# init stuff
game = Game()
io = Interface()
# tiles
tile_grass = Tile('grass', '.', 3)
tile_dirt  = Tile('dirt',  '.', 2)
tile_tree  = Tile('tree',  'Y', 2)
tile_floor = Tile('floor', '.', 0)
tile_wall  = Tile('wall',  '#', 0)
tile_door  = Tile('door',  '+', 2)
# creatures
player = Creature('player', '@', 4)
player.x = 15
player.y = 10
# map
current_map = Map()
current_map.spray(tile_tree, 16)
current_map.spray(tile_dirt, 64)
current_map.room(12, 4, 7, 4)

# begin main loop
while game.over == False:
  # clear the screen
  io.clear()
  # render everything
  current_map.draw()
  player.draw()
  # debug stuff
  win_main.move(0, 41)
  win_main.addstr("Turns: " + str(game.turn) )
  win_main.move(1, 41)
  win_main.addstr("Player X: " + str(player.x) )
  win_main.move(2, 41)
  win_main.addstr("Player Y: " + str(player.y) )
  # handle input
  io.getinput()

# end main loop

# exit
io.close()