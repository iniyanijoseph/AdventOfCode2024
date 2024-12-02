# aoc 2024 1.py

from os import pread
import pathlib
import sys
from collections import defaultdict
import parse

sys.setrecursionlimit(10000)

def parse(puzzle_input):
    """Parse input."""
    file = open(f'{puzzle_input}.txt',mode='r')

    # List of strings/2d Array of characters
    inp = file.read().split("\n")
    # Remove blank lines
    # inp = [i for i in inp if i != ""]

    # Convert each line to an integer
    # inp = [int(line) for line in file.read().split()]

    # 2D Array of numbers
    # inp = [list(map(int, line.split())) for line in file.read().split("\n")]

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
    return -1

def part2(inp):
    """Solve part 2."""
    return -1

if __name__ == "__main__":
    inp = parse(2)
    print(inp)
    print("SO1____________")
    a = part1(inp)
    print(a)
    print("EO1____________")
    print("SO2")
    a = part2(inp)
    print(a)
    print("EO2____________")


