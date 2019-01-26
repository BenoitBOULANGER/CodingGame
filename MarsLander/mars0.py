import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def stabilize_vertical_speed(v_speed, target_speed):
    if v_speed < target_speed:
        return 4
    else:
        return 3


surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
    if y > 2400:
        power = 0
    elif y > 2300:
        power = 2
    elif y > 2000:
        power = 3
    elif y > 1500:
        power = stabilize_vertical_speed(v_speed, 30)
    elif y > 1000:
        power = stabilize_vertical_speed(v_speed, 20)
    else:
        power = stabilize_vertical_speed(v_speed, 10)

    print("0 %s" % power)
