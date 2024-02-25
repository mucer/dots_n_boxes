from mapper import Mapper

def test_index_for_pos():
    
    SIZE = 3
    sides = {
        "left":  [
            [12, 13, 14],
            [11, 10, 9],
            [0, 1, 2]
        ],
        "front": [
            [15, 16, 17],
            [8, 7, 6],
            [3, 4, 5]
        ],
        "right": [
            [14, 9, 2],
            [13, 10, 1],
            [12, 11, 0]
        ],
        "top": [
            [5, 4, 3],
            [6, 7, 8],
            [17, 16, 15]
        ],
    }

    mapper = Mapper(SIZE)

    for side_name in sides:
        side = sides[side_name]
        for y in range(SIZE):
            for x in range(SIZE):
                should = side[SIZE - y - 1][x]
                print(f"{x}x{y}@{side_name} should be {should}")
                assert mapper.pos_to_pixel(side_name, x, y)[1] == should

