import sys
import math

max_speed=0
light_count = 0
lights=[]

def get_input():
    global max_speed
    global light_count
    global lights

    max_speed = int(input())
    light_count = int(input())

    for i in range(light_count):
        distance, duration = [int(j) for j in input().split()]
        lights.append([distance, duration])

# return true is the light is green when the car arrives
def verify_light(speed, light):
    distance = light[0]
    frequence = light[1]

    value = (distance * 36) / (speed * frequence * 10)
    return ((int(value) % 2) == 0)

def verify_lights(speed, lights):
    for light in lights:
        if not verify_light(speed, light):
            return False
    return True

def main():
    get_input()
    speed = max_speed
    while speed > 0:
        print("testing speed:", speed, file=sys.stderr )
        if verify_lights(speed, lights):
            print(speed)
            exit(0)
        else:
            speed = speed - 1

if __name__ == '__main__':
    main()