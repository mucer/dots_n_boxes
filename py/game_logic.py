from enums import Direction
from side import Side
from cell_pos import CellPos

class Player:
    def __init__(self, pos, direction):
        self.pos = pos
        self.direction = direction

class PlayerCellData:
    def __init__(self):
        self.at_position = False
        self.active_trail = False

class GameLogic:
    def __init__(self, size):
        self.size = size
        self.cells = {}
           
        front = Side("front", self.size)
        top = Side("top", self.size)
        left = Side("left", self.size)
        right = Side("right", self.size)
        self.players = [
            Player(CellPos(front, 0, 0), Direction.RIGHT),
            # Player(CellPos(front, size - 1, size - 1), Direction.LEFT)
        ]

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

        self.sides = [front, left, right, top]

        for side in self.sides:
            for x in range(self.size):
                for y in range(self.size):
                    pos = CellPos(side, x, y)
                    self.cells[pos] = [PlayerCellData() for _ in range(len(self.players))]

    def tick(self):
        self.move_players()
        self.update_matrix()

    def get_cell_data(self, pos):
        return self.cells[pos]

    def get_player(self, p):
        return self.players[p]

    def move_players(self):
        for player in self.players:
            player.pos.move(player.direction)

    def update_matrix(self):
       for pos in self.cells: 
            self.update_cell(pos, self.cells[pos])

    def update_cell(self, pos, cell):
        for i in range(len(self.players)): 
            player = self.players[i]
            cell[i].at_position = pos == player.pos
            if cell[i].at_position and not cell[i].active_trail:
                cell[i].active_trail = True
