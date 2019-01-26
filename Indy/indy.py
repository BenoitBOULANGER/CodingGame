import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

cave=[]

def get_input():
    # w: number of columns.
    # h: number of rows.
    w, h = [int(i) for i in input().split()]
    for i in range(h):
        # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
        line = input()
        cave.append(line.split())
    # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).
    ex = int(input())

def display_cave():
    for line in cave:
        print(line, file=sys.stderr)

def get_next_position(x, y, pos):
    current_piece=cave[y][x]

    print("current_piece", current_piece, file=sys.stderr )

    if current_piece == "1" or current_piece == "8" or current_piece == "3" or current_piece == "7" or current_piece == "9" or current_piece == "12" or current_piece == "13":
        return x, y+1
    elif current_piece == "2" or current_piece == "6":
        if pos == "LEFT":
            return x+1, y
        else:
            return x-1,y
    elif current_piece == "4":
        if pos == "TOP":
            return x-1, y
        else:
            return x, y+1
    elif current_piece == "5":
        if pos == "TOP":
            return x+1, y
        else:
            return x, y+1
    elif current_piece == "10":
        return x - 1, y
    elif current_piece == "11":
        return x + 1, y
    else:
        return 0,0

def main():
    get_input()
    display_cave()

    # game loop
    while True:
        xi, yi, pos = input().split()
        xi = int(xi)
        yi = int(yi)

        next_x, next_y = get_next_position(xi,yi, pos)
        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)

        # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
        print(next_x, next_y)

if __name__ == '__main__':
    main()