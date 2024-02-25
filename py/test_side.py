from enums import Direction
from side import Side
from cell_pos import CellPos

SIZE = 3
        
front = Side("front", SIZE)
top = Side("top", SIZE)
left = Side("left", SIZE)
right = Side("right", SIZE)

front.attach_top(top, Direction.DOWN)
front.attach_left(left, Direction.RIGHT)
front.attach_right(right, Direction.LEFT)

top.attach_down(front, Direction.UP)
top.attach_left(left, Direction.UP)
top.attach_right(right, Direction.UP)

left.attach_right(front, Direction.LEFT)
left.attach_top(top, Direction.LEFT)

right.attach_left(front, Direction.RIGHT)
right.attach_top(top, Direction.RIGHT)

def test_borders():
    max = SIZE - 1

    pos = CellPos(front, 0, 0)
    pos.move(Direction.DOWN)
    assert str(pos) == str(CellPos(front, 0, 0))

    pos = CellPos(left, 0, 0)
    pos.move(Direction.LEFT)
    assert str(pos) == str(CellPos(left, 0, 0))

    pos = CellPos(right, max, 0)
    pos.move(Direction.RIGHT)
    assert str(pos) == str(CellPos(right, max, 0))

    pos = CellPos(top, 0, max)
    pos.move(Direction.UP)
    assert str(pos) == str(CellPos(top, 0, max))

def test_edges():
    max = SIZE - 1

    pos = CellPos(front, 0, max)
    pos.move(Direction.LEFT)
    assert str(pos) == str(CellPos(left, max, max))

    pos.move(Direction.UP)
    assert str(pos) == str(CellPos(top, 0, 0))

    pos.move(Direction.DOWN)
    assert str(pos) == str(CellPos(front, 0, max))

    pos.move(Direction.UP)
    assert str(pos) == str(CellPos(top, 0, 0))

    pos.move(Direction.LEFT)
    assert str(pos) == str(CellPos(left, max, max))

    pos.move(Direction.RIGHT)
    assert str(pos) == str(CellPos(front, 0, max))

    pos = CellPos(front, max, max)
    
    pos.move(Direction.RIGHT)
    assert str(pos) == str(CellPos(right, 0, max))

    pos.move(Direction.UP)
    assert str(pos) == str(CellPos(top, max, 0))

    pos.move(Direction.DOWN)
    assert str(pos) == str(CellPos(front, max, max))

    pos.move(Direction.UP)
    assert str(pos) == str(CellPos(top, max, 0))

    pos.move(Direction.RIGHT)
    assert str(pos) == str(CellPos(right, 0, max))
    
    pos.move(Direction.LEFT)
    assert str(pos) == str(CellPos(front, max, max))

    