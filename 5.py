# aoc 2024 1.py

import sys
from collections import defaultdict

sys.setrecursionlimit(int(1E9))

import networkx as nx
import matplotlib.pyplot as plt

class GraphVisualization:
    def __init__(self):
        self.visual = []

    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    def visualize(self):
        G = nx.DiGraph(directed=True)
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()

def parse(puzzle_input):
    """Parse input."""
    file = open(f'{puzzle_input}.txt',mode='r')

    inp = file.read().splitlines()

    i = 0
    g = defaultdict(set)
    while(inp[i] != ""):
        # String, String pairs
        a, b = map(int, inp[i].split("|"))

        g[a].add(b)
        i += 1
    i += 1
    q = []
    while i < len(inp):
        q.append(list(map(int, inp[i].split(","))))
        i += 1

    file.close()

    return (g, q)

def topsort(g):
    lst = []
    visited = set()

    def dfs(v):
        visited.add(v)
        for n in sorted(list(g[v]), reverse=True):
            if n not in visited:
                dfs(n)
        lst.append(v)

    for v in sorted(list(g.keys()), reverse=True):
        if v not in visited:
            dfs(v)

    return lst[::-1]


def part1(inp):
    """Solve part 1."""
    s = 0
    for _, q in enumerate(inp[1]):
        incorrect = False
        for p in range(len(q)-1):
            if q[p+1] not in inp[0][q[p]]:
                incorrect = True
        s += q[(len(q)-1)//2] if not incorrect else 0

    return s

def part2(inp):
    """Solve part 2."""
    s = 0
    top = topsort(inp[0])
    for p in range(len(top)-1):
        if top[p+1] not in inp[0][top[p]]:
            print("NOT TOPSORT")

    for _, q in enumerate(inp[1]):
        incorrect = False

        for p in range(len(q)-1):
            if q[p+1] not in inp[0][q[p]]:
                incorrect = True

        indeg = defaultdict(int)
        for a in q:
            for b in q:
                if b in inp[0][a]:
                    indeg[b] += 1

        # s += sorted(q, key=lambda v: top.index(v))[(len(q)-1)//2] if incorrect else 0
        if incorrect:
            for v in indeg:
                if indeg[v] == len([k for k in inp[0][v] if k in q]):
                    s += v
    return s


if __name__ == "__main__":
    inp = parse(5)
    print(inp)
    print("SO1____________")
    a = part1(inp)
    print(a)
    print("EO1____________")
    print("SO2")
    a = part2(inp)
    print(a)



    print("EO2____________")


