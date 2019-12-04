#!/usr/bin/env python3
# Day 3: Crossed Wires
# Part 2
# Pass a file with the input as an argument

import sys
import numpy as np

xmap = np.zeros((60000, 60000), dtype=np.int16)
center_pos = 30000

def draw_paths(wire1, wire2):
    total_steps1 = 0
    total_steps2 = 0
    current = [center_pos, center_pos]
    least_steps = 10000
    for direction in wire1:
        if direction[0] == 'U':
            steps = int(direction[1:])
            for i in range(steps):
                current[1] += 1
                total_steps1 += 1
                if xmap[current[0], current[1]] == 0:
                    xmap[current[0], current[1]] = total_steps1

        elif direction[0] == 'D':
            steps = int(direction[1:])
            for i in range(steps):
                current[1] -= 1
                total_steps1 += 1
                if xmap[current[0], current[1]] == 0:
                    xmap[current[0], current[1]] = total_steps1

        elif direction[0] == 'L':
            steps = int(direction[1:])
            for i in range(steps):
                current[0] -= 1
                total_steps1 += 1
                if xmap[current[0], current[1]] == 0:
                    xmap[current[0], current[1]] = total_steps1

        elif direction[0] == 'R':
            steps = int(direction[1:])
            for i in range(steps):
                current[0] += 1
                total_steps1 += 1
                if xmap[current[0], current[1]] == 0:
                    xmap[current[0], current[1]] = total_steps1

    current = [center_pos, center_pos]

    for direction in wire2:
        if direction[0] == 'U':
            steps = int(direction[1:])
            for i in range(steps):
                current[1] += 1
                total_steps2 += 1
                if xmap[current[0], current[1]] != 0:
                    least_steps = min(least_steps,
                                      xmap[current[0], current[1]] + total_steps2)

        elif direction[0] == 'D':
            steps = int(direction[1:])
            for i in range(steps):
                current[1] -= 1
                total_steps2 += 1
                if xmap[current[0], current[1]] != 0:
                    least_steps = min(least_steps,
                                      xmap[current[0], current[1]] + total_steps2)

        elif direction[0] == 'L':
            steps = int(direction[1:])
            for i in range(steps):
                current[0] -= 1
                total_steps2 += 1
                if xmap[current[0], current[1]] != 0:
                    least_steps = min(least_steps,
                                      xmap[current[0], current[1]] + total_steps2)

        elif direction[0] == 'R':
            steps = int(direction[1:])
            for i in range(steps):
                current[0] += 1
                total_steps2 += 1
                if xmap[current[0], current[1]] != 0:
                    least_steps = min(least_steps,
                                      xmap[current[0], current[1]] + total_steps2)

    return least_steps

def main():
    file_name = sys.argv[1]
    with open(file_name, 'r') as file:
        wire1 = file.readline().rstrip().split(',')
        wire2 = file.readline().rstrip().split(',')
        print(draw_paths(wire1, wire2))


if __name__ == "__main__":
    main()