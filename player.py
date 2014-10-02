class Player:
  def __init__(self, name, char, color):
    self.name  = name
    self.char  = char
    self.color = color
    self.x, self.y = -1, -1
    self.inv = []
