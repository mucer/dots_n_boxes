from game_logic import GameLogic
from cell_pos import CellPos
from colorama import Fore, Back, Style
from enums import Direction
import time

SIZE = 3
game = GameLogic(SIZE)

def main():
    # print started to the console
    print("started")
    i = 0
    while True:
        game.tick()
        print_matrix()

        i += 1

        if (i == 2 * SIZE):
            game.get_player(0).direction = Direction.LEFT
        if (i == 3 * SIZE):
            game.get_player(0).direction = Direction.UP
        if (i == 4 * SIZE):
            game.get_player(0).direction = Direction.RIGHT


        # print(Fore.RED + "Hello", end=" ")
        # print(Fore.BLUE + "world")
        # print(Style.RESET_ALL)  # Reset color to default

        time.sleep(1)  # Sleep for 1 second

def print_matrix():
    for side in game.sides:
        print(side.name)
        for y in reversed(range(side.size)):
            for x in range(side.size):
                pos = CellPos(side, x, y)
                cell = game.get_cell_data(pos)
                if (cell[0].at_position):
                    print(Fore.RED + "X", end="")
                #elif (cell[1].at_position):
                #    print(Fore.BLUE + "X", end="")
                else:
                    print(Fore.WHITE + ".", end="")
            print()
        print(Style.RESET_ALL)
    print()
    

main()