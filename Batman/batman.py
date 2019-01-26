import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
width, high = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

max_positions=[[0,width-1],[0,high-1]]

def is_up(bomb_dir):
    return "U" in bomb_dir

def is_down(bomb_dir):
    return "D" in bomb_dir

def is_left(bomb_dir):
    return "L" in bomb_dir

def is_right(bomb_dir):
    return "R" in bomb_dir

def get_next_horizontal_position(max_positions, current_x, bomb_dir):

    if is_right(bomb_dir):
        max_positions[0][0] = current_x
    elif is_left(bomb_dir):
        max_positions[0][1] = current_x
    else:
        return int(current_x)
    return int((max_positions[0][0] + max_positions[0][1]) / 2)

def get_next_vertical_position(max_positions, current_y, bomb_dir):

    if is_down(bomb_dir):
        max_positions[1][0] = current_y
    elif is_up(bomb_dir):
        max_positions[1][1] = current_y
    else:
        return int(current_y)
    return int((max_positions[1][0] + max_positions[1][1] ) / 2 )



def main():
    current_x = x0
    current_y = y0

    while True:
        bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
        print(max_positions, file=sys.stderr)
        print("bomb: ", bomb_dir, file=sys.stderr)

        next_x = get_next_horizontal_position(max_positions, x0, bomb_dir)
        next_y = get_next_vertical_position(max_positions, y0, bomb_dir)

        print(next_x, next_y)

if __name__ == '__main__':
    main()