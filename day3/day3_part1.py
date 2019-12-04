#!/usr/bin/env python3
# Day 3: Crossed Wires
# Part 1
# Pass a file with the input as an argument

import sys
import numpy as np
# import turtle

# turtle.delay(0)
# turtle.ht()

xmap = np.zeros((60000, 60000), dtype=np.int8)
center_pos = 30000

def draw_paths(wire1, wire2):
    current = [center_pos, center_pos]
    # turtle.pencolor("blue")
    for direction in wire1:
        if direction[0] == 'U':
            # turtle.setheading(0)
            steps = int(direction[1:])
            # turtle.forward(0.1 * steps)
            for i in range(steps):
                current[1] += 1
                xmap[current[0], current[1]] = 1

        elif direction[0] == 'D':
            # turtle.setheading(180)
            steps = int(direction[1:])
            # turtle.forward(0.1 * steps)
            for i in range(steps):
                current[1] -= 1
                xmap[current[0], current[1]] = 1

        elif direction[0] == 'L':
            # turtle.setheading(270)
            steps = int(direction[1:])
            # turtle.forward(0.1 * steps)
            for i in range(steps):
                current[0] -= 1
                xmap[current[0], current[1]] = 1

        elif direction[0] == 'R':
            # turtle.setheading(90)
            steps = int(direction[1:])
            # turtle.forward(0.1 * steps)
            for i in range(steps):
                current[0] += 1
                xmap[current[0], current[1]] = 1

    current = [center_pos, center_pos]

    dist = 10000
    # turtle.penup()
    # turtle.setpos(0,0)
    # turtle.pendown()
    # turtle.pencolor("red")
    for direction in wire2:
        if direction[0] == 'U':
            # turtle.setheading(0)
            steps = int(direction[1:])
            # turtle.forward(0.1 * steps)
            for i in range(steps):
                current[1] += 1
                if xmap[current[0], current[1]] == 1:
                    dist = min(dist, abs(center_pos - current[0]) + abs(center_pos - current[1]))

        elif direction[0] == 'D':
            # turtle.setheading(180)
            steps = int(direction[1:])
            # turtle.forward(0.1 * steps)
            for i in range(steps):
                current[1] -= 1
                if xmap[current[0], current[1]] == 1:
                    dist = min(dist, abs(center_pos - current[0]) + abs(center_pos - current[1]))

        elif direction[0] == 'L':
            # turtle.setheading(270)
            steps = int(direction[1:])
            # turtle.forward(0.1 * steps)
            for i in range(steps):
                current[0] -= 1
                if xmap[current[0], current[1]] == 1:
                    dist = min(dist, abs(center_pos - current[0]) + abs(center_pos - current[1]))

        elif direction[0] == 'R':
            # turtle.setheading(90)
            steps = int(direction[1:])
            # turtle.forward(0.1 * steps)
            for i in range(steps):
                current[0] += 1
                if xmap[current[0], current[1]] == 1:
                    dist = min(dist, abs(center_pos - current[0]) + abs(center_pos - current[1]))
    return dist


def main():
    file_name = sys.argv[1]
    with open(file_name, 'r') as file:
        wire1 = file.readline().rstrip().split(',')
        wire2 = file.readline().rstrip().split(',')
        print(draw_paths(wire1, wire2))


if __name__ == "__main__":
    main()