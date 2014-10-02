class World:
  # init map with grass
  def __init__(self):
    self.width = 40
    self.height = 16
    self.grid = []
    self.items = []
    self.monsters = []
  # return char from tile
  def getchar(self, y, x):
    return self.grid[y][x].char
