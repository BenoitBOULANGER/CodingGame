#!/usr/bin/env python3

import sys
import math

data=[]
neighbours=[]

def display_inputs():
    print(data)

def display_neighbours():
    for line in neighbours:
        for value in line:
            print(value, end=' ')
        print('')

def get_input():
    global data;

    width = int(input())  # the number of cells on the X axis
    height = int(input())  # the number of cells on the Y axis
    for i in range(height):
        line = list(input())  # width characters, each either 0 or .
        data.append(line)

def get_neighbours(data, x1, y1, width, height):
    global neighbours;

    x2=x1+1
    y2=y1
    found = False
    while found != True and x2 < width:
        if data[y2][x2] == '0':
            found = True
        else:
            x2 = x2 + 1
    if x2 == width:
        x2=-1
        y2=-1

    x3=x1
    y3=y1+1
    found = False
    while found != True and y3 < height:
        if data[y3][x3] == '0':
            found = True
        else:
            y3 = y3 + 1
    if y3 >= height:
        x3=-1
        y3=-1

    neighbours.append([x1,y1,x2, y2, x3, y3])

def solve(data):
    height=len(data)
    width=len(data[0])
    for y1 in range(0, height):
        for x1 in range(0, width):
            if data[y1][x1] == '0':
                get_neighbours(data, x1, y1, width, height)


def main():
    get_input()
    solve(data)
    display_neighbours()
    
if __name__ == '__main__':
    main()
