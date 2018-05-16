
MAP_WIDTH = 10
MAP_HEIGHT = 12

NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)


no_go_blocks = [
    (5,11),
    (0,4),(1,4),(2,4)
]

direction_order = [NORTH, EAST, SOUTH, WEST]
RIGHT_HAND = 1
LEFT_HAND = -1


def get_next_direction(direction, preference):
    current_dir_idx = direction_order.index(direction)
    next_dir_idx = current_dir_idx + preference
    if next_dir_idx >= len(direction_order):
        next_dir_idx = 0
    elif next_dir_idx < 0:
        next_dir_idx = len(direction_order) - 1
    return direction_order[next_dir_idx]


def new_pos(current_pos, direction):
    return current_pos[0] + direction[0], current_pos[1] + direction[1]


def can_move(current_pos, direction):
    newpos = new_pos(current_pos, direction)
    bounds_check = -1 < newpos[0] < MAP_WIDTH and -1 < newpos[1] < MAP_HEIGHT
    if not bounds_check:
        return False

    try:
        if no_go_blocks.index(newpos) > -1:
            return False
    except ValueError:
        pass

    return True

if __name__ == "__main__":
    test_pos = (0, 0)
    assert (not can_move(test_pos, NORTH))
    assert (not can_move(test_pos, WEST))
    assert (can_move(test_pos, EAST))
    assert (can_move(test_pos, SOUTH))

    test_pos = (MAP_WIDTH - 1, MAP_HEIGHT - 1)
    assert (can_move(test_pos, NORTH))
    assert (can_move(test_pos, WEST))
    assert (not can_move(test_pos, EAST))
    assert (not can_move(test_pos, SOUTH))

    assert (get_next_direction(NORTH, RIGHT_HAND) == EAST)
    assert (get_next_direction(EAST, RIGHT_HAND) == SOUTH)
    assert (get_next_direction(SOUTH, RIGHT_HAND) == WEST)
    assert (get_next_direction(WEST, RIGHT_HAND) == NORTH)
    assert (get_next_direction(NORTH, LEFT_HAND) == WEST)

    start_pos = (MAP_WIDTH - 1, MAP_HEIGHT - 1)
    position = start_pos
    direction = WEST
    handedness = RIGHT_HAND
    moving = True
    while moving:
        print('@{x} {y}'.format(x=position[0], y=position[1]))
        try_turn_left = get_next_direction(direction, LEFT_HAND)
        if can_move(position, try_turn_left):
            direction = try_turn_left
        if can_move(position, direction):
            position = new_pos(position, direction)
        else:
            direction = get_next_direction(direction, handedness)
        if position == start_pos:
            print('Stopped @ {x} {y}'.format(x=position[0], y=position[1]))
            moving = False
