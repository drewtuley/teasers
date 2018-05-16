import copy
from itertools import product

# solve Coin Collecting Tuesday Teaser by brute force approach
offsets = [
    # array of tuples giving offsets (x,y) to check around a given point
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1)
]


def validate_position(cmap, row, col, value_to_check):
    coin_count = 0
    for o in offsets:
        o_row = row + o[1]
        o_col = col + o[0]
        if -1 < o_row < 12 and -1 < o_col < 8:
            value_under_test = cmap[(o_row * 8) + o_col]
            if value_under_test == 'O':
                coin_count += 1
    return coin_count == value_to_check


def build_test_map(cmap, prod):
    test_map = copy.copy(cmap)
    map_idx = 0
    for c in prod:
        while test_map[map_idx] != '':
            map_idx += 1
        test_map[map_idx] = c
    return test_map


def check_map(cmap):
    success = True
    for r in range(0, 12):
        for c in range(0, 8):
            p = cmap[(r * 8) + c]
            if p not in ['X', 'O']:
                v = validate_position(cmap, r, c, p)
                if not v:
                    success = False
    return success


def print_map(cmap):
    for r in range(0, 12):
        l = ''
        for c in range(0, 8):
            l += str(cmap[(r * 8) + c])
        print(l)


if __name__ == "__main__":
    coin_map = ['', '', 3, '', '', 1, 2, '',
                '', 3, '', '', 3, 3, '', '',
                3, '', 2, '', 2, '', '', 2,
                '', '', 1, '', '', 2, '', '',
                3, '', '', '', '', 1, '', 1,
                '', '', '', '', '', '', '', '',
                'X', 'X', 1, '', 2, '', 2, '',
                'X', 0, 'X', '', 4, '', '', '',
                'X', 'X', 'X', 3, '', '', 4, '',
                '', '', '', '', '', '', '', 1,
                2, 2, 2, 3, 'X', 'X', 3, '',
                '', '', '', '', 'X', 0, 'X', '']

    assert (len(coin_map) == 96)

    known_solution = [
        'O','O','O','X','O',
        'O','X','O','O','X',
        'X','X','O','O',
        'O','O','X','X','X','X',
        'X','X','X','X','X',
        'O','X','X','X','X','X','O','X',
        'O','X','X',
        'X','O','X','X',
        'O','O','X',
        'O','X','X','O','O','O','O',
        'X',
        'O','X','X','O','O'
    ]
    assert(len(known_solution) == 56)
    assert(check_map(build_test_map(coin_map, known_solution)))

    attempt = 1
    for prod in product(['X', 'O'], repeat=56):
        print('Attempt: {}'.format(attempt))
        attempt += 1
        test_map = build_test_map(coin_map, prod)
        if check_map(test_map):
            print_map(test_map)
            break
