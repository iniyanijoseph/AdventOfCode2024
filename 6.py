# aoc 2024 1.py

from os import pread
import pathlib
from tqdm import tqdm
import sys
from collections import defaultdict
import parse
import math
from collections import deque

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
    # inp = [list(map(int, line.split())) for line in file.read().splitlines()]

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
    grd = (0, 0)
    dir = "^"
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if(inp[i][j] == "^"):
                grd = (i, j)


    next = {"^":(-1, 0), "<":(0,-1),">":(0,1),"v":(1,0)}
    visited = {grd}
    a, b = grd
    while(0 <= a < len(inp) and 0 <= b < len(inp[0])):
        if inp[a][b] != "#":
            grd = (a, b)
        else:
            if dir == "^":
                dir = ">"
            elif dir == ">":
                dir = "v"
            elif dir == "v":
                dir = "<"
            elif dir == "<":
                dir = "^"
        visited.add(grd)
        a, b = (grd[0] + next[dir][0], grd[1] + next[dir][1])

    return len(visited)

def checkCycle(inp):
    """Solve part 1."""
    grd = (0, 0)
    dir = "^"
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if(inp[i][j] == "^"):
                grd = (i, j)

    next = {"^":(-1, 0), "<":(0,-1),">":(0,1),"v":(1,0)}
    visited = defaultdict(set)
    a, b = grd
    while(0 <= a < len(inp) and 0 <= b < len(inp[0])):
        if dir in visited[(a, b)]:
            # print((a, b))
            return True

        visited[(a, b)].add(dir)
        if inp[a][b] != "#":
            grd = (a, b)
        else:
            if dir == "^":
                dir = ">"
            elif dir == ">":
                dir = "v"
            elif dir == "v":
                dir = "<"
            elif dir == "<":
                dir = "^"

        a, b = (grd[0] + next[dir][0], grd[1] + next[dir][1])

    return False

def part2(inp):
    """Solve part 1."""
    s = 0
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            prev = inp[i][j]
            if prev != "^" and prev != "#":
                inp[i] = inp[i][:j] + "#" + inp[i][j+1:]
                s += checkCycle(inp)
                inp[i] = inp[i][:j] + prev + inp[i][j+1:]

    return s

if __name__ == "__main__":
    inp = parse(6)
    print(inp)
    print("SO1____________")
    a = part1(inp)
    print(a)
    print("EO1____________")
    print("SO2")
    a = part2(inp)
    print(a)
    print("EO2____________")


