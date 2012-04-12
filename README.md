This is a very simple Grid/Point system in Python, using a combination
of subclasses (Grid(dict), and Point(complex)) to handle the internals.

Example:

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

    print 'Resize grid to 5 x 5'
    grid.resize(5, 5)

    print grid

...which outputs:

    Original grid setup
       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8
    -----------------------------------
     1 |   |   |   |   |   |   |   |
     2 |   |   |   |   |   |   |   |
     3 |   |   |   |   |   |   |   |
     4 |   |   |   | X | O |   |   |
     5 |   |   |   | O | X |   |   |
     6 |   |   |   |   |   |   |   |
     7 |   |   |   |   |   |   |   |
     8 | A | B | C |   |   |   |   |
    -----------------------------------

    Swap (1,8) and (3, 8)
    Move (2,8) to (2,1)
       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8
    -----------------------------------
     1 |   | B |   |   |   |   |   |
     2 |   |   |   |   |   |   |   |
     3 |   |   |   |   |   |   |   |
     4 |   |   |   | X | O |   |   |
     5 |   |   |   | O | X |   |   |
     6 |   |   |   |   |   |   |   |
     7 |   |   |   |   |   |   |   |
     8 | C |   | A |   |   |   |   |
    -----------------------------------

    Resize grid to 5 x 5
       | 1 | 2 | 3 | 4 | 5
    -----------------------
     1 |   | B |   |   |
     2 |   |   |   |   |
     3 |   |   |   |   |
     4 |   |   |   | X | O
     5 |   |   |   | O | X
    -----------------------




