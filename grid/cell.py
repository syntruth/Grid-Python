class Cell:
  def __init__(self, point, content):
    self.point   = point
    self.content = content

  def as_tuple(self):
    return (self.point.x, self.point.y, self.content)

  def __str__(self):
    return "%s: %s" % (self.point, self.content)

  def __repr__(self):
    p = self.point.__repr__()
    c = self.content.__repr__()
    return "Cell(%s, %s)" % (p, c)

