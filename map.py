class Map:
  # init map with grass
  def __init__(self):
    self.width = 40
    self.height = 16
    self.grid = [[ tile_grass
      for y in range(self.height) ]
        for x in range(self.width) ]
  # return char from tile
  def getchar(self, y, x):
    return self.grid[y][x].char
  # render the map
  def draw(self):
    for x, col in enumerate(self.grid):
      for y, cell in enumerate(col):
        if cell.color > 6:
          cons.setbold()
        cons.setcolor(cell.color)
        cons.putchar(y, x, cell.char)
        cons.unsetcolor(cell.color)
        cons.unsetbold()
  # add a single tile
  def add(self, tile, x, y):
    self.grid[x][y] = tile
  # random spray of tiles
  def spray(self, tile, n):
    for x in range(n):
      rx = random.randint(0, self.width - 1)
      ry = random.randint(0, self.height - 1)
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
