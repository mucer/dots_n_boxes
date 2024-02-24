enum class Direction { UP,
                       DOWN,
                       LEFT,
                       RIGHT };
enum class Side { FRONT,
                  LEFT,
                  TOP,
                  RIGHT };

struct Player {
  int x, y;
  Direction direction;
};

struct CellPlayerData {
  bool atPosition, activeTrail, ownedBy;
};

class GameLogic {
public:
  GameLogics() {
  }
  ~GameLogic() {
    delete[] data;
    delete[] players;
  }

  void tick() {
    movePlayers();
    updateMatrix();
  }

  CellPlayerData* getCellPlayerData(int x, int y, int p) {
    return &data[y * cols + x + p * rows * cols];
  }

  Player* getPlayer(int p) {
    return &players[p];
  }

  void init() {
    int cellCount = rows * cols * numPlayers;
    data = new CellPlayerData[cellCount];
    for (int i = 0; i < cellCount; i++)
      data[i] = { false, false, false };
    players = new Player[2];
    players[0] = { 0, 0, Direction::RIGHT };
    players[1] = { 1, 1, Direction::LEFT };

    updateMatrix();
  }

private:
  int numPlayers = 2, rows = 4, cols = 4;
  CellPlayerData* data;
  Player* players;

  void movePlayers() {
    for (int i = 0; i < numPlayers; i++)
      movePlayer(&players[i]);
  }

  void movePlayer(Player* player) {
    switch (player->direction) {
      case Direction::UP:
        if (player->y > 0) player->y--;
        break;
      case Direction::DOWN:
        if (player->y < rows - 1) player->y++;
        break;
      case Direction::LEFT:
        if (player->x > 0) player->x--;
        break;
      case Direction::RIGHT:
        if (player->x < cols - 1) player->x++;
        break;
    }
  }

  void updateMatrix() {
    for (int y = 0; y < rows; y++) {
      for (int x = 0; x < cols; x++) {
        for (int p = 0; p < numPlayers; p++) {
          updateCell(x, y, p);
        }
      }
    }
  }

  void updateCell(int x, int y, int p) {
    Player* player = getPlayer(p);
    CellPlayerData* cell = getCellPlayerData(x, y, p);
    cell->atPosition = x == player->x && y == player->y;
    if (cell->atPosition) {
      cell->activeTrail = true;
    }
  }
};