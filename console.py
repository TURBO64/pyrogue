from unicurses import *

class Console:
  def __init__(self):
    stdscr = initscr()
    noecho()
    cbreak()
    curs_set(False)
    start_color()
    use_default_colors()
    init_pair( 0, COLOR_WHITE,   COLOR_BLACK)
    init_pair( 1, COLOR_RED,     COLOR_BLACK)
    init_pair( 2, COLOR_YELLOW,  COLOR_BLACK)
    init_pair( 3, COLOR_GREEN,   COLOR_BLACK)
    init_pair( 4, COLOR_CYAN,    COLOR_BLACK)
    init_pair( 5, COLOR_BLUE,    COLOR_BLACK)
    init_pair( 6, COLOR_MAGENTA, COLOR_BLACK)
    init_pair( 7, COLOR_WHITE,   COLOR_BLACK)
    init_pair( 8, COLOR_RED,     COLOR_BLACK)
    init_pair( 9, COLOR_YELLOW,  COLOR_BLACK)
    init_pair(10, COLOR_GREEN,   COLOR_BLACK)
    init_pair(11, COLOR_CYAN,    COLOR_BLACK)
    init_pair(12, COLOR_BLUE,    COLOR_BLACK)
    init_pair(13, COLOR_MAGENTA, COLOR_BLACK)
  def close(self):
    nocbreak()
    echo()
    endwin()
  def clear(self):
    refresh()
  def putchar(self, y, x, char):
    move(y, x)
    addstr(char)
  def setcolor(self, n):
    attron(color_pair(n) )
  def unsetcolor(self, n):
    attroff(color_pair(n) )
  def setbold(self):
    attron(A_BOLD)
  def unsetbold(self):
    attroff(A_BOLD)
