from point import Point
from cell  import Cell

from random import randint

class GridError(Exception):
  pass

class GridBoundsError(GridError):
  pass

class Grid(dict):

  def __init__(self, sizex=3, sizey=3, default=None):
    self.sizex   = abs(sizex)
    self.sizey   = abs(sizey)
    self.default = default

    self._set_corners()

  def points(all=False):
    if all:
      all = []

      for x in range(1, self.sizex + 1):
        for y in range(1, self.sizey + 1):
          all.append(Point(x, y))

      return all
    else:
      return self.keys()

  def is_sane(self, point):
    return (1 <= point.x <= self.sizex) and (1 <= point.y <= self.sizey)

  def set_cell(self, point, data):
    if self.is_sane(point):
      self[point] = Cell(point, data)

  def get_cell(self, point, include_empty=False):
    if self.has_key(point):
      return self[point]
    elif include_empty:
      return Cell(point, self.default)

    return None

  def get_cells(self, points=[], include_empty=False):
    cells = []

    for point in points:
      if self.is_sane(point):
        cell = self.get_cell(point, include_empty)

        if cell or include_empty:
          cells.append(cell)

    return cells

  def get_row(self, y, include_empty=False):
    cells = []

    for x in range(1, self.sizex + 1):
      point = Point(x, y)
      cell  = self.get_cell(point, include_empty)

      if cell or include_empty:
        cells.append(cell)

    return cells

  def get_column(self, x, include_empty=False):
    cells = []

    for y in range(1, self.sizey + 1):
      point = Point(x, y)
      cell  = self.get_cell(point, include_empty)

      if cell or include_empty:
        cells.append(cell)

    return cells

  def clear_cell(self, point):
    if self.has_key(point):
      del self[point]

  def clear_all(self):
    for point in self.keys():
      del self[point]

  def neighbors(self, point, include_empty=False):
    cells = []

    for vector in Point.vectors:
      if vector == Point.Center:
        continue

      vp = Point.from_vector(vector)
      np = point + vp

      if self.is_sane(np):
        cell = self.get_cell(np, include_empty)

        if cell or include_empty:
          cells.append(cell)

    return cells

  def traverse(self, point, vector, include_empty=False):
    cells  = []
    vector = Point.from_vector(vector)

    while self.is_sane(point):
      cell = self.get_cell(point)

      if cell or include_empty:
        cells.append(point)

      point += vector

    return cells

  def swap_cells(self, point1, point2):
    for point in [point1, point2]:
      if not self.is_sane(point):
        raise GridBoundsError, '%s out of bounds!' % point

    p1key = self.has_key(point1)
    p2key = self.has_key(point2)

    # We have both keys, so swap their contents!
    if p1key and p2key:
      d1 = self[point1].content
      d2 = self[point2].content

      self[point1].content = d2
      self[point2].content = d1

    # We only have the first key, so put 
    # it in point2's slot.
    elif p1key:
      self.set_cell(point2, self[point1].content)
      self.clear_cell(point1)

    # We only have the second key, so put 
    # it in point1's slot.
    elif p2key:
      self.set_cell(point1, self[point2].content)
      self.clear_cell(point2)

    # Else, we don't have either key...
    else:
      return False

    # We swapped something, so return True.
    return True

  def move_cell(self, fp, tp):
    for point in [fp, tp]:
      if not self.is_sane(point):
        raise GridBoundsError, '%s out of bounds!' % point

    if self.has_key(fp):
      self.set_cell(tp, self[fp].content)
      self.clear_cell(fp)
      return True
    else:
      return False

  def contents(self, include_empty=False):
    cells = []

    for point in self.keys():
      cell = self.get_cell(point, include_empty)

      if cell or include_empty:
        cells.append(cell)

    return cells

  def populate(self, cells=[]):
    n = 0

    for cell in cells:
      point   = cell.point
      content = cell.content

      if self.is_sane(point):
        self.set_cell(point, content)
        n += 1

    return n

  def random_cell(self, include_empty=False):
    x = randint(1, self.sizex)
    y = randint(1, self.sizey)
    return self.get_cell(Point(x, y), include_empty)

  def random_cells(self, how_many, include_empty=False):
    cells = []

    for i in range(how_many):
      cells.append(self.random_cell(include_empty))
      
    return cells

  def number_of_cells(self, include_empty=True):
    if include_empty:
      return self.sizex * self.sizey
    else:
      return len(self.keys())

  def resize(self, sizex=3, sizey=3):
    self.sizex = abs(sizex)
    self.sizey = abs(sizey)

    self._set_corners()
  
    for point in self.keys():
      if not self.is_sane(point):
        del self[point]

  def copy(self):
    newgrid = Grid(self.sizex, self.sizey, self.default)

    for cell in self.contents():
      newgrid.set_cell(cell.point, cell.content)

    return newgrid

  def sub(self, point, width=2, height=None):
    # Default to an N x N grid.
    if not height:
      height = width

    grid  = Grid(width, height, self.default)
    cells = []

    sx = point.x
    sy = point.y

    for x in range(1, width + 1):
      for y in range(1, height + 1):
        tmpx = sx + (x - 1)
        tmpy = sy + (y - 1)
        cell = self.get_cell(Point(tmpx, tmpy))

        if cell:
          grid.set_cell(Point(x, y), cell.content)

    return grid

  def print_grid(self):
    print self

  def _set_corners(self):
    self.bl = Point(1, 1)
    self.tl = Point(1, self.sizey)
    self.br = Point(self.sizex, 1)
    self.tr = Point(self.sizex, self.sizey)

  def __str__(self):
    rets = []
    szy  = self.sizey + 1
    fmt  = '|'.join([' %s '] * szy)
    line = '-' * len(fmt.replace('%', ''))
    top  = [' ']
    
    for x in range(1, self.sizex + 1):
      top.append(x)

    rets.append(fmt % tuple(top))
    rets.append(line)

    for y in range(1, szy):
      row = [str(y)]

      for cell in self.get_row(y, True):
        row.append(cell.content)

      rets.append(fmt % tuple(row))

    rets.append(line)
    
    return '\n'.join(rets)

  def __repr__(self):
    x = self.sizex
    y = self.sizey
    d = self.default

    if isinstance(d, str):
      d = '"%s"' % d

    return "Grid(%s, %s, %s)" % (x, y, d)

if __name__ == '__main__':
  grid  = Grid(8, 8, ' ')
  point = Point(2, 8)

  grid.set_cell(point - 1, 'A')
  grid.set_cell(point,     'B')
  grid.set_cell(point + 1, 'C')

  grid.set_cell(Point(4, 5), "O")
  grid.set_cell(Point(5, 5), "X")
  grid.set_cell(Point(4, 4), "X")
  grid.set_cell(Point(5, 4), "O")

  print 'Original grid setup'
  print grid

  print 'Swap (1,8) and (3, 8)'
  print 'Move (2,8) to (2,1)'
  grid.swap_cells(Point(1, 8), Point(3, 8))
  grid.move_cell(Point(2, 8), Point(2, 1))

  print grid
 
  print 'Get a subgrid of 3 x 3 starting at (4, 4) and set (3, 3) to #'
  subg = grid.sub(Point(4, 4), 3)
  subg.set_cell(Point(3, 3), '#')

  print subg

  print 'Resize original grid to 5 x 5'
  grid.resize(5, 5)

  print grid
