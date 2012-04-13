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

  @staticmethod
  def from_vector(vector):
    return Point(*vector)

  def __init__(self, x, y):
    super(complex, self).__init__(x, y)
    self.x = x
    self.y = y

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

