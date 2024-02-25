
#define SIZE 16

enum class Direction
{
  UP,
  DOWN,
  LEFT,
  RIGHT
};
enum class Side
{
  FRONT,
  LEFT,
  TOP,
  RIGHT
};

struct CellPos
{
  Side side;
  int x, y;

  bool operator==(const CellPos &other) const
  {
    return side == other.side && x == other.x && y == other.y;
  }

  CellPos moveClone(Direction direction)
  {
    CellPos newPos = {side, x, y};
    newPos.moveSelf(direction);
    return newPos;
  }

  void moveSelf(Direction direction)
  {
    CellPos newPos = {side, x, y};
    switch (direction)
    {
    case Direction::UP:
      if (y >= SIZE - 1)
      {
        if (side == Side::FRONT)
        {
          side = Side::TOP;
          y = 0;
        }
        else if (side == Side::LEFT)
        {
          side = Side::TOP;
          y = SIZE - x - 1;
          x = 0;
        }
        else if (side == Side::RIGHT)
        {
          side = Side::TOP;
          y = x;
          x = SIZE - 1;
        }
        side = Side::TOP;
      }
      else
      {
        y++;
      }
      break;
    case Direction::DOWN:
      if (y <= 0)
      {
        if (side == Side::TOP)
        {
          side = Side::FRONT;
          y = SIZE - 1;
        }
      }
      else
      {
        y--;
      }
      break;
    case Direction::LEFT:
      if (x <= 0)
      {
        if (side == Side::FRONT)
        {
          side = Side::LEFT;
          x = SIZE - 1;
        }
        else if (side == Side::TOP)
        {
          side = Side::LEFT;
          x = SIZE - y - 1;
          y = SIZE - 1;
        }
        else if (side == Side::RIGHT)
        {
          side = Side::FRONT;
          x = SIZE - 1;
        }
      }
      else
      {
        x--;
      }
      break;
    case Direction::RIGHT:
      if (x >= SIZE - 1)
      {
        if (side == Side::FRONT)
        {
          side = Side::RIGHT;
          x = 0;
        }
        else if (side == Side::TOP)
        {
          side = Side::RIGHT;
          x = y;
          y = SIZE - 1;
        }
        else if (side == Side::LEFT)
        {
          side = Side::FRONT;
          x = 0;
        }
      }
      else
      {
        x++;
      }
      break;
    }
  }
};

struct Player
{
  CellPos pos;
  Direction direction;
};

struct CellPlayerData
{
  bool atPosition, activeTrail, ownedBy;
};

class GameLogic
{
public:
  GameLogic()
  {
    initArrays();
    updateMatrix();
  }
  ~GameLogic()
  {
    delete[] data;
    delete[] players;
  }

  void tick()
  {
    movePlayers();
    updateMatrix();
  }

  CellPlayerData *getCellPlayerData(CellPos pos, int p)
  {
    return &data[pos.y * SIZE + pos.x + p * SIZE * SIZE];
  }

  Player *getPlayer(int p)
  {
    return &players[p];
  }

private:
  int numPlayers = 2;
  CellPlayerData *data;
  Player *players;

  void initArrays()
  {
    int cellCount = SIZE * SIZE * numPlayers;
    data = new CellPlayerData[cellCount];
    for (int i = 0; i < cellCount; i++)
      data[i] = {false, false, false};
    players = new Player[2];
    players[0] = {{Side::FRONT, 0, 0}, Direction::RIGHT};
    players[1] = {{Side::FRONT, 1, 1}, Direction::LEFT};
  }

  void movePlayers()
  {
    for (int i = 0; i < numPlayers; i++)
    {
      Player *player = &players[i];
      player->pos.moveSelf(player->direction);
    }
  }

  void updateMatrix()
  {
    for (int y = 0; y < SIZE; y++)
    {
      for (int x = 0; x < SIZE; x++)
      {
        for (int p = 0; p < numPlayers; p++)
        {
          CellPos pos = {Side::FRONT, x, y};
          updateCell(pos, p);
        }
      }
    }
  }

  void updateCell(CellPos pos, int p)
  {
    Player *player = getPlayer(p);
    CellPlayerData *cell = getCellPlayerData(pos, p);
    cell->atPosition = pos == player->pos;
    if (cell->atPosition && !cell->activeTrail)
    {
      cell->activeTrail = true;
    }
  }
};