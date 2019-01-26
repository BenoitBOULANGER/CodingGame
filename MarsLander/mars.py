import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
surface=[]

def display(x, y, h_speed, v_speed, fuel, current_rotate, current_power, land_high, land_x0, land_x1, relative_high):
    print("current pos", x, y, file=sys.stderr)
    print ("target landing", land_x0, land_x1, land_high, file=sys.stderr)
    print ("relative_high", relative_high, file=sys.stderr)

def get_input():
    surface_n = int(input())  # the number of points used to draw the surface of Mars.
    for i in range(surface_n):
        # land_x: X coordinate of a surface point. (0 to 6999)
        # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
        surface.append([int(j) for j in input().split()])

def get_landing_zone(surface):
    previous_x=-1
    previous_y=-1
    for x,y in surface:
        if y == previous_y:
            return(previous_x, x, y)
        else:
            previous_x = x
            previous_y = y

# see below
def get_y(x, x0, y0, x1,y1):
    return int(y1 + (x1-x)*(y0-y1)/(x1-x0))

def get_current_ground_high(current_x):
    previous_x=-1
    previous_y=-1
    for x,y in surface:
        if current_x >= previous_x and current_x <= x:
            return get_y(current_x, previous_x, previous_y, x, y)
        else:
            previous_x = x
            previous_y = y

# return the miximum ground high between x_init and x_end
def get_max_ground_high(x_init, x_end):
    max = 0
    for x,y in surface:
        if x > x_init and x < x_end:
            if y > max:
                max = y
    return max;

def get_highs(x, y, land_x0, land_x1, land_high):
    ground_high = get_current_ground_high(x)
    relative_high = y - ground_high
    highest_point = 0
    if x < land_x0:
        highest_point = get_max_ground_high(x, land_x0)
    else:
        highest_point = get_max_ground_high(land_x1, x)
    minimum_high = max(land_high, highest_point)

    print("ground, relative, highest, land, minimun", ground_high, relative_high, highest_point, land_high, minimum_high , file=sys.stderr)
    return relative_high, minimum_high



def stabilize_vertical_speed(v_speed, target_speed):
    print("stabilize v_speed", v_speed, target_speed, file=sys.stderr)
    if v_speed < target_speed:
        return 4
    else:
        return 3

def get_power(high, v_speed):
    if high > 2500:
        power = stabilize_vertical_speed(v_speed, -50)
    else:
        power = stabilize_vertical_speed(v_speed, -35)
    return power

def get_rotation_angle(x, x_target, high, h_speed):
    if high > 50:
        target_speed = int((x+x_target)/(2*(x-x_target))*20)
        print("target speed", target_speed, h_speed, file=sys.stderr)
        print("x & x_target", x, x_target, file=sys.stderr)

        if x < x_target:
            rotate=min(90, h_speed-target_speed)
        else:
            rotate=max(-90, h_speed-target_speed)
    else:
        rotate = 0

    return rotate

def set_power(rotate, current_rotate, h_speed):
    #print("rotate, current_rotate, h_speed", rotate, current_rotate, h_speed, file=sys.stderr)

    if rotate > 0 and current_rotate > -1:
        return 4
    elif rotate < 0 and current_rotate <1:
        return 4
    else:
        return 0

def move_horizontally(x, land_x0, land_x1, h_speed, target_speed, current_rotate, v_speed, relative_high, minimum_high):
    print("relative_high", relative_high, file=sys.stderr)

    if relative_high < 500:
        return 4, 0

    if h_speed > 40 and v_speed > -42 and relative_high > 1000:
        if current_rotate > 0:
            return 4, 80
        else:
            return 0, 80
    if h_speed < -40 and v_speed > -42 and relative_high > 1000:
        if current_rotate < 0:
            return 4, -80
        else:
            return 0, -80

    if x < land_x0:
        if h_speed < target_speed:
            rotate = -17
        elif h_speed > 50:
            rotate = 17
        else:
            rotate = 0

    elif x > land_x1:
        if h_speed > -target_speed:
            rotate = 17
        elif h_speed < -50:
            rotate = -17
        else:
            rotate = 0

    #if rotate == 0:
    #    x_target=int((land_x0 + land_x1)/2)
    #    power, rotate = get_down(x, x_target, relative_high, v_speed, h_speed, current_rotate)
    #else:
    power = set_power(rotate, current_rotate, h_speed)

    return power, rotate


def get_down(x, x_target, relative_high, v_speed, h_speed, current_rotate):

    print("relative_high", relative_high, file=sys.stderr)
    rotate = 0

    if h_speed > 40 and v_speed > -40 and relative_high > 1000:
        if current_rotate > 0:
            return 4, 80
        else:
            return 0, 80
    if h_speed < -40 and v_speed > -40 and relative_high > 1000:
        if current_rotate < 0:
            return 4, -80
        else:
            return 0, -80

    if x < x_target - 500:
        if h_speed > 15:
            rotate = 17
        elif h_speed < -15:
            rotate = -17
    elif x > x_target + 500:
        if h_speed < -15:
            rotate = -17
        elif h_speed > 15:
            rotate = 17

    if relative_high < 100:
        rotate = 0

    power = get_power(relative_high, v_speed)
    print("rotate", rotate, file=sys.stderr)
    print("power", power, file=sys.stderr)

    return power, rotate

def get_command(x, y,
                h_speed, v_speed,
                fuel,
                current_rotate,
                current_power,
                land_high,
                land_x0, land_x1):

    relative_high, minimum_high = get_highs(x, y, land_x0, land_x1, land_high)
    #print("relative minimun high", relative_high, minimum_high, file=sys.stderr)
    #display(x, y, h_speed, v_speed, fuel, current_rotate, current_power, land_high, land_x0, land_x1, relative_high)

    middle_of_the_landing_zone=(land_x0+land_x1)/2

    # we are not in the landing zone
    if x < land_x0 or x > land_x1:
        power, rotate = move_horizontally(x, land_x0, land_x1, h_speed, 30, current_rotate, v_speed, relative_high, minimum_high)
    else:
        power, rotate = get_down(x, middle_of_the_landing_zone, relative_high, v_speed, h_speed, current_rotate)

    return rotate, power

def main():
    get_input()
    land_x0, land_x1, land_high = get_landing_zone(surface)

    # game loop
    while True:
        # h_speed: the horizontal speed (in m/s), can be negative.
        # v_speed: the vertical speed (in m/s), can be negative.
        # fuel: the quantity of remaining fuel in liters.
        # rotate: the rotation angle in degrees (-90 to 90).
        # power: the thrust power (0 to 4).
        x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

        angle, power = get_command(x, y, h_speed, v_speed, fuel, rotate, power, land_high, land_x0, land_x1)

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)

        # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
        print(angle, power)


if __name__ == '__main__':
    main()