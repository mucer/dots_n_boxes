from enums import Direction

class CellPos:
    def __init__(self, side, x, y):
        self.side = side
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.x}x{self.y}@{self.side.name}"
    def __eq__(self, other):
        return self.side == other.side and self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.side.name, self.x, self.y))

    def move(self, direction):
        old = self.clone()
        if direction == Direction.UP:
            if (self.y >= self.side.size - 1):
                return self.side.transfer_up(self)
            else:
                self.y += 1

        elif direction == Direction.DOWN:
            if (self.y <= 0):
                return self.side.transfer_down(self)
            else:
                self.y -= 1

        elif direction == Direction.LEFT:
            if (self.x <= 0):
                return self.side.transfer_left(self)
            else:
                self.x -= 1

        elif direction == Direction.RIGHT:
            if (self.x >= self.side.size - 1):
                return self.side.transfer_right(self)
            else:
                self.x += 1
        
        return direction
        raise ValueError('went out of matrix')

        
    
    def clone(self):
        return CellPos(self.side, self.x, self.y)
    