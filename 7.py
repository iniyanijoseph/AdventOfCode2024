# aoc 2024 1.py

from os import pread
import pathlib
import sys
from collections import defaultdict
import parse
from tqdm import tqdm
import pyperclip
import math

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

    inp = [(int(i.split(":")[0]), list(map(int, (i.split(":")[1]).split()))) for i in inp]

    file.close()

    return inp

def pm(li, i, s, t):
    if len(li) == i:
        return s == t

    return pm(li, i+1, s + li[i], t) + pm(li, i+1, s * li[i], t)

def part1(inp):
    """Solve part 1."""
    s = 0
    for k in inp:
        if pm(k[1], 1, k[1][0], k[0]):
            s += k[0]
    return s

def numcat(a,b):
    x = int(math.pow(10,(int(math.log(b,10)) + 1)) * a + b)
    y = int(f"{a}{b}")
    z = int(str(a) + str(b))

    if x==y==z:
        return x
    else:
        print(a, "+", b, x, y, z)

def pmc(li, i, s, t):
    if len(li) == i:
        return s == t

    return pmc(li, i+1, s + li[i], t) + pmc(li, i+1, s * li[i], t) + pmc(li, i+1, numcat(s, li[i]), t)

def part2(inp):
    """Solve part 2."""
    s = 0
    for k in tqdm(inp):
        if pmc(k[1], 1, k[1][0], k[0]):
            s += k[0]
    return s

if __name__ == "__main__":
    inp = parse(7)
    # print(inp)
    print("SO1____________")
    a = part1(inp)
    print(a)
    print("EO1____________")
    print("SO2")
    b = part2(inp)
    print(b)
    pyperclip.copy(str(a) if b != -1 else str(b))
    print("EO2____________")


