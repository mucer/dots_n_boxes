// my first program in C++
#include <iostream>
#include <bitset>

struct Color
{
    int r, g, b;
};
enum Direction
{
    UP,
    DOWN,
    LEFT,
    RIGHT
};

struct Player
{
    Color color;
    int x, y;
    Direction direction;
    bool trailActive;
};
struct CellPlayerData
{
    bool atPosition, activeTrail, ownedBy;
};

class Matrix
{
public:
    Matrix(int rows, int cols) : rows(rows), cols(cols)
    {
        // init data with 0
        numPlayers = 2;
        data = new CellPlayerData[rows * cols * numPlayers];
        for (int i = 0; i < rows * cols; i++)
            data[i] = {0, 0, 0};
        players = new Player[]{
            {{255, 0, 0}, 0, 0, RIGHT, true},
            {{0, 255, 0}, 3, 3, LEFT, true},
        };
        updateMatrix();

        // std::cout << "players: " << sizeof(players) << " player: " << sizeof(Player) << " numPlayers: " << numPlayers << std::endl;
    }
    ~Matrix()
    {
        delete[] data;
        delete[] players;
    }

    void tick()
    {
        movePlayers();
        updateMatrix();
        print();
    }

    CellPlayerData* getCellPlayerData(int x, int y, int p)
    {
        return &data[y * cols + x + p * rows * cols];
    }

    Player* getPlayer(int p)
    {
        return &players[p];
    }

private:
    int rows, cols;
    CellPlayerData *data;
    Player *players;
    int numPlayers;

    void movePlayers()
    {
        for (int i = 0; i < numPlayers; i++)
            movePlayer(&players[i]);
    }

    void movePlayer(Player* player)
    {
        switch (player->direction)
        {
        case UP:
            if (player->y > 0) player->y--;
            break;
        case DOWN:
            if (player->y < rows - 1) player->y++;
            break;
        case LEFT:
            if (player->x > 0) player->x--;
            break;
        case RIGHT:
            if (player->x < cols - 1) player->x++;
            break;
        }
    }

    void updateMatrix()
    {
        for (int y = 0; y < rows; y++)
        {
            for (int x = 0; x < cols; x++)
            {
                for (int p = 0; p < numPlayers; p++)
                {
                    updateCell(x, y, p);
                }
            }
        }
    }

    void updateCell(int x, int y, int p)
    {
        Player* player = getPlayer(p);
        CellPlayerData* cell = getCellPlayerData(x, y, p);
        cell->atPosition = x == player->x && y == player->y;
        if (cell->atPosition && player->trailActive) {
            cell->activeTrail = true;
        }
    }

    void print()
    {
        for (int y = 0; y < rows; y++)
        {
            for (int x = 0; x < cols; x++) 
            {
                for (int p = 0; p < numPlayers; p++)
                {
                    printCell(x, y, p);
                }
                std::cout << " ";
            }
            std::cout << std::endl;
        }
        std::cout << std::endl;
    }

    void printCell(int x, int y, int p)
    {
        CellPlayerData* cell = getCellPlayerData(x, y, p);
        std::cout << "\x1B[3" << (p + 1) << "m"
                  << (cell->atPosition ? 'P' : '-')
                  << (cell->activeTrail ? 'T' : '-')
                  << (cell->ownedBy ? 'O' : '-')
                  << "\033[0m";
    }
};

int main()
{
    Matrix matrix(4, 4);
    matrix.tick();
    matrix.getPlayer(0)->direction = DOWN;
    matrix.tick();
    matrix.getPlayer(0)->direction = LEFT;
    matrix.tick();
    std::cout << "Hello World!";

    
    
    printf("\n");
}
