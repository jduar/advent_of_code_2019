#!/usr/bin/env python3
# Day 2: 1202 Program Alarm
# Part 2
# Pass a file with the input as an argument

import sys

def intcode(int_list):
    for i in range(0, 100):
        for j in range(0, 100):
            copy_list = int_list.copy()
            opcode = 0
            copy_list[1] = i
            copy_list[2] = j
            for opcode in range(0, len(copy_list)-1, 4):
                param1 = copy_list[opcode + 1]
                param2 = copy_list[opcode + 2]
                out = copy_list[opcode + 3]
                if copy_list[opcode] == 1:
                    copy_list[out] = copy_list[param1] + copy_list[param2]
                elif copy_list[opcode] == 2:
                    copy_list[out] = copy_list[param1] * copy_list[param2]
                elif copy_list[opcode] == 99:
                    if copy_list[0] == 19690720:
                        return 100 * i + j
                    break
                else:
                    break


def main():
    file_name = sys.argv[1]
    with open(file_name, 'r') as file:
        # Reading the line, stripping it of '\n', splitting it
        # and then turning everything into int elements.
        code_list = file.readline().rstrip().split(',')
    code_list = list(map(int, code_list))

    result = intcode(code_list)
    print("Answer: " + str(result))


if __name__ == "__main__":
    main()