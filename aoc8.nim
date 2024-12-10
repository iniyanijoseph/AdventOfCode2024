import strutils, sequtils, sugar, std/tables, sets
import lib/vector

var inp = collect(newSeq):
  for line in lines("8.txt"):
    line

var freqs = initTable[char, HashSet[Vector[int]]]()
var occupied = HashSet[Vector[int]]()

for i in 0..<len(inp):
  for j in 0..<len(inp[i]):
    if inp[i][j] != '.':
      if inp[i][j] notin freqs:
        freqs[inp[i][j]] = initHashSet[Vector[int]]()

      var a = newVector[int](i, j)
      freqs[inp[i][j]].incl(a)
      occupied.incl(a)

var locs = initHashSet[Vector[int]]()

for i in freqs.keys:
  for x in freqs[i]:
    for y in freqs[i]:

      var dif = x-y
      #[
      # Part 1
      if x + dif notin freqs[i]:
        locs.incl(x + dif)
      if y + dif notin freqs[i]:
        locs.incl(y + dif)
      if x - dif notin freqs[i]:
        locs.incl(x - dif)
      if y - dif notin freqs[i]:
        locs.incl(y - dif)
      ]#

      for j in -100..100:
        if not (x + dif == y):
          locs.incl(x + dif*j)

var l = 0
for i in locs:
  if (0 <= i.x and i.x < len(inp)) and (0 <= i.y and i.y < len(inp[0])):
    inp[i.x][i.y] = if inp[i.x][i.y] == '.': '#' else: inp[i.x][i.y]
    l += 1

echo inp.join("\n")

echo l

