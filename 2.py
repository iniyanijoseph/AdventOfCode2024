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
    # inp = file.read().splitlines()
    # Remove blank lines
    # inp = [i for i in inp if i != ""]

    # Convert each line to an integer
    # inp = [int(line) for line in file.read().splitlines()]

    # 2D Array of numbers
    inp = [list(map(int, line.split())) for line in file.read().splitlines()]

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

    """
    Docnotes
    ### map(lambda a: operation(a), inp)
    ### filter(lambda a: operation(a), inp)
    ### reduce(lambda a: operation(a), inp)
    """
    file.close()

    return inp

def part1(inp):
    """Solve part 1."""
    s = 0
    for li in inp:
        t = [li[i]-li[i-1] for i in range(1, len(li))]
        s += 1 if (all([i == -1 or i == -2 or i == -3 for i in t]) or all([i == 1 or i == 2 or i == 3 for i in t])) else 0

    return s

def part2(inp):
    """Solve part 2."""
    s = 0
    for li in inp:
        for j in range(len(li)):
            k = li[:j-1]+li[j:]
            if j == 0:
                k = li[0:-1]
            t = [k[i]-k[i-1] for i in range(1, len(k))]
            print(t,k if (all([i == -1 or i == -2 or i == -3 for i in t]) or all([i == 1 or i == 2 or i == 3 for i in t])) else 0)
            s += 1 if (all([i == -1 or i == -2 or i == -3 for i in t]) or all([i == 1 or i == 2 or i == 3 for i in t])) else 0
            if (all([i == -1 or i == -2 or i == -3 for i in t]) or all([i == 1 or i == 2 or i == 3 for i in t])):
                break;

    return s

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


