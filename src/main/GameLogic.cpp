enum class Direction { UP,
                       DOWN,
                       LEFT,
                       RIGHT };
enum class Side { FRONT,
                  LEFT,
                  TOP,
                  RIGHT };

struct CellPos {
  Side side;
  int x, y;

  bool operator==(const CellPos& other) const {
    return side == other.side && x == other.x && y == other.y;
  }
};

struct Player {
  CellPos pos;
  Direction direction;
};

struct CellPlayerData {
  bool atPosition, activeTrail, ownedBy;
};

class GameLogic {
public:
  GameLogic() {
    initArrays();
    updateMatrix();
  }
  ~GameLogic() {
    delete[] data;
    delete[] players;
  }

  void tick() {
    movePlayers();
    updateMatrix();
  }

  CellPlayerData* getCellPlayerData(CellPos pos, int p) {
    return &data[pos.y * cols + pos.x + p * rows * cols];
  }

  Player* getPlayer(int p) {
    return &players[p];
  }

  void movePos(CellPos* pos, Direction direction) {
    switch (direction) {
      case Direction::UP:
        if (pos->y > 0) pos->y--;
        break;
      case Direction::DOWN:
        if (pos->y < rows - 1) pos->y++;
        break;
      case Direction::LEFT:
        if (pos->x > 0) pos->x--;
        break;
      case Direction::RIGHT:
        if (pos->x < cols - 1) pos->x++;
        break;
    }
  }

private:
  int numPlayers = 2, rows = 4, cols = 4;
  CellPlayerData* data;
  Player* players;

  void initArrays() {
    int cellCount = rows * cols * numPlayers;
    data = new CellPlayerData[cellCount];
    for (int i = 0; i < cellCount; i++)
      data[i] = { false, false, false };
    players = new Player[2];
    players[0] = { { Side::FRONT, 0, 0 }, Direction::RIGHT };
    players[1] = { { Side::FRONT, 1, 1 }, Direction::LEFT };
  }

  void movePlayers() {
    for (int i = 0; i < numPlayers; i++) {
      Player* player = &players[i];
      movePos(&player->pos, player->direction);
    }
  }

  void updateMatrix() {
    for (int y = 0; y < rows; y++) {
      for (int x = 0; x < cols; x++) {
        for (int p = 0; p < numPlayers; p++) {
          CellPos pos = { Side::FRONT, x, y };
          updateCell(pos, p);
        }
      }
    }
  }

  void updateCell(CellPos pos, int p) {
    Player* player = getPlayer(p);
    CellPlayerData* cell = getCellPlayerData(pos, p);
    cell->atPosition = pos == player->pos;
    if (cell->atPosition && !cell->activeTrail) {
      cell->activeTrail = true;
    }
  }
};