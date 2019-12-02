#!/usr/bin/env python3
# Day 1 - Problem 1
# Pass a file with the input as an argument

import sys

def fuel(mass):
    return (mass // 3) - 2

def main():
    total_fuel = 0
    file_name = sys.argv[1]
    with open(file_name, 'r') as file:
        for line in file:
            total_fuel += fuel(int(line))
    print(total_fuel)

if __name__ == "__main__":
    main()