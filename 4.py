# aoc 2024 1.py

from os import pread
import pathlib
import sys
from collections import defaultdict
import parse
import re
from functools import reduce

sys.setrecursionlimit(10000)

def parse(puzzle_input):
    """Parse input."""
    file = open(f'{puzzle_input}.txt',mode='r')

    # List of strings/2d Array of characters
    inp = file.read().splitlines()
    # Remove blank lines
    # inp = [i for i in inp if i != ""]

    # Convert each line to an integer
    # inp = [int(line) for line in file.read().splitlines()]

    # 2D Array of numbers
    # inp = [line.split() for line in file.read().splitlines()]

    # Rotate 2D Array
    # inp = [list(elem) for elem in zip(*inp[::-1])]

    # Dictionary of string pairs a b
    # inp = {a:b for a, b in input().split()}

    # Graph of input given edges
    """
    inp = file.read().split("\n")
    inp = [i for i in inp if i != ""]
    print(inp)
    g = defaultdict(set)
    for line in inp:
        print(line)
        # String, String pairs
        a, b = line.split()
        # Int, Int pairs
        a, b = map(int, line.split())

        g[a].add(b)
    """

    # Regex match input
    """
    pattern = parse.compile("{a} text {b} text {c} text.")
    [pattern.search(i).named for i in file.read().split("\n") if i != ""]
    """

    file.close()

    return inp

def part1(inp):
    """Solve part 1."""
    horz = sum([len(re.findall(r"XMAS", i)) for i in inp])
    horz += sum([len(re.findall(r"SAMX", i)) for i in inp])
    inp = [reduce(lambda x,y :x+y, elem) for elem in zip(*inp[::-1])]
    vert = sum([len(re.findall(r"XMAS", i)) for i in inp])
    vert += sum([len(re.findall(r"SAMX", i)) for i in inp])

    inp = [reduce(lambda x,y :x+y, elem) for elem in zip(*inp[::-1])]
    inp = [reduce(lambda x,y :x+y, elem) for elem in zip(*inp[::-1])]

    leftdiag = [e*" " + i + (len(inp)-e-1)*" " for e, i in enumerate(inp)]
    leftdiag = [reduce(lambda x,y :x+y, elem) for elem in zip(*leftdiag[::-1])]

    ld = sum([len(re.findall(r"XMAS", i)) for i in leftdiag])
    ld += sum([len(re.findall(r"SAMX", i)) for i in leftdiag])

    rightdiag = [(len(inp)-e-1)*" " + i + " "*e for e, i in enumerate(inp)]
    rightdiag = [reduce(lambda x,y :x+y, elem) for elem in zip(*rightdiag[::-1])]

    rd = sum([len(re.findall(r"XMAS", i)) for i in rightdiag])
    rd += sum([len(re.findall(r"SAMX", i)) for i in rightdiag])

    print(horz, vert, ld, rd)

    return horz + vert + ld + rd

def part2(inp):
    """Solve part 2."""
    s  = 0
    for i in range(len(inp)-2):
        for j in range(len(inp[i])-2):
            if(inp[i][j] == "M" and inp[i][j+2] == "S" and inp[i+1][j+1] == "A" and inp[i+2][j] == "M" and inp[i+2][j+2] == "S"):
                s += 1
            elif(inp[i][j] == "M" and inp[i][j+2] == "M" and inp[i+1][j+1] == "A" and inp[i+2][j] == "S" and inp[i+2][j+2] == "S"):
                s += 1
            elif(inp[i][j] == "S" and inp[i][j+2] == "S" and inp[i+1][j+1] == "A" and inp[i+2][j] == "M" and inp[i+2][j+2] == "M"):
                s += 1
            elif(inp[i][j] == "S" and inp[i][j+2] == "M" and inp[i+1][j+1] == "A" and inp[i+2][j] == "S" and inp[i+2][j+2] == "M"):
                s += 1

    return s

if __name__ == "__main__":
    inp = parse(4)
    print(inp)
    print("SO1____________")
    a = part1(inp)
    print(a)
    print("EO1____________")
    print("SO2")
    a = part2(inp)
    print(a)
    print("EO2____________")


