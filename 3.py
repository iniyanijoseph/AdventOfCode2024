# aoc 2024 1.py

from os import pread
import pathlib
import sys
from collections import defaultdict
import parse
import re

sys.setrecursionlimit(10000)

def parse(puzzle_input):
    """Parse input."""
    file = open(f'{puzzle_input}.txt',mode='r')

    # List of strings/2d Array of characters
    inp = file.read()
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
    #inp=inp.replace(")mul", ") mul").replace("(mul", "mul")

    file.close()

    return inp

def part1(inp):
    """Solve part 1."""
    inp = re.findall(r"mul\(\d*,\d*\)", inp)
    s = 0
    for i in inp:
        a, b = i.split(",")
        b = int(b[:-1])
        a = int(a[4:])
        print(a, b)
        s += a*b
    return s

def part2(inp):
    """Solve part 2."""
    inp = [i.group() for i in re.finditer(r"(don\'t\(\))|(mul\(\d*,\d*\))|(do\(\))", inp)]
    print(inp)
    s = 0
    ignore = False
    for i in inp:
        if(i == "do()"):
            ignore = False
        elif(i == "don't()"):
            ignore = True
        elif not ignore:
            a, b = i.split(",")
            b = int(b[:-1])
            a = int(a[4:])
            print(a, b)
            s += a*b

    return s


if __name__ == "__main__":
    inp = parse(3)
    print(inp)
    print("SO1____________")
    a = part1(inp)
    print(a)
    print("EO1____________")
    print("SO2")
    a = part2(inp)
    print(a)
    print("EO2____________")


