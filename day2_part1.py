#!/usr/bin/env python3
# Day 2: 1202 Program Alarm
# Part 1
# Pass a file with the input as an argument

import sys

def intcode(int_list):
    opcode = 0
    while int_list[opcode] != 99:
        op1 = int_list[int_list[opcode + 1]]
        op2 = int_list[int_list[opcode + 2]]
        out = int_list[opcode + 3]
        if int_list[opcode] == 1:
            int_list[out] = op1 + op2
        elif int_list[opcode] == 2:
            int_list[out] = op1 * op2
        opcode += 4
    return int_list


def main():
    file_name = sys.argv[1]
    with open(file_name, 'r') as file:
        # Reading the line, stripping it of '\n', splitting it
        # and then turning everything into int elements.
        code_list = file.readline().rstrip().split(',')
    code_list = list(map(int, code_list))

    result = intcode(code_list)
    print("Answer: " + str(result[0]))


if __name__ == "__main__":
    main()