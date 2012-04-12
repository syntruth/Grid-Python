class Point(complex):
  TopLeft     = (-1,  -1)
  Top         = (0,   -1)
  TopRight    = (1,   -1)
  Left        = (-1,  0)
  Center      = (0,   0)
  Right       = (1,   0)
  BottomLeft  = (-1,  1)
  Bottom      = (0,   1)
  BottomRight = (1,   1)

  vectors = [
    TopLeft,    Top,    TopRight,
    Left,       Center, Right,
    BottomLeft, Bottom, BottomRight
  ]

  def x(self):
    return self.real

  def y(self):
    return self.imag

  def neighbors(self):
    results = []
    for coords in self.vectors:
      if coords == self.Center:
        continue
      vector = Point(*coords)
      results.append(self + vector)

    return results

  def traverse(self, vector, limit=1):
    results = []
    vector  = Point(*vector)
    point   = Point(self.real, self.imag)
    
    while limit:
      limit -= 1
      point  = point + vector
      results.append(point)

    return results

  def __add__(self, other):
    real = self.real + other.real
    imag = self.imag + other.imag
    return Point(real, imag)

  def __sub__(self, other):
    real = self.real - other.real
    imag = self.imag - other.imag
    return Point(real, imag)
  
  def __str__(self):
    return "(%.1f, %.1f)" % (self.real, self.imag)

  def __repr__(self):
    return "Point(%s, %s)" % (self.real, self.imag)

if __name__ == '__main__':
  p1 = Point(4,  5)
  p2 = Point(-1, 2)

  print 'Neighbors of %s:' % p1
  for p in p1.neighbors():
    print p
  print ''

  print 'Traversing from %s towards top right 5 units:' % p2
  for p in p2.traverse(Point.TopRight, 5):
    print p
  print ''


