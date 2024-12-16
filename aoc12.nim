import strutils, sequtils, sugar, sets, lib/vector, tables

var inp = collect:
  for line in lines("12.txt"):
    line

var table = initTable[HashSet[Vector[int]], char]()
var found = initHashSet[Vector[int]]()


for i in 0..<inp.len:
  for j in 0..<inp[i].len:
    var current = initHashSet[Vector[int]]()

    proc floodFill(i : int, j : int, ch : char) =
      let pos = newVector[int](i, j)
      if i >= 0 and i < inp.len and j >= 0 and j < inp[i].len:
        if pos notin found:
          if ch == inp[i][j]:
            current.incl(pos)
            found.incl(pos)
            floodFill(i+1, j, ch)
            floodFill(i-1, j, ch)
            floodFill(i, j+1, ch)
            floodFill(i, j-1, ch)

    floodFill(i, j, inp[i][j])
    table[current] = inp[i][j]

block:
  var s = 0
  for group, ch in table:
    if group.len == 0:
      continue
    var boundary = initTable[Vector[int], int]()
    for point in group:
      let down = point + newVector(0, 1)
      let up = point + newVector(0, -1)
      let left = point + newVector(-1, 0)
      let right = point + newVector(1, 0)

      proc incl(pos : Vector[int]) =
        if pos notin group:
          if pos notin boundary:
            boundary[pos] = 0
          boundary[pos] += 1

      incl(up)
      incl(down)
      incl(left)
      incl(right)

    var l = 0
    for point, count in boundary:
      l += count

    s += l * group.len

  echo s

block:
  var s = 0
  for group, ch in table:
    if group.len == 0:
      continue
    var boundary = initHashSet[Vector[int]]()
    for point in group:
      let down = point + newVector(0, 1)
      let up = point + newVector(0, -1)
      let left = point + newVector(-1, 0)
      let right = point + newVector(1, 0)

      proc incl(pos : Vector[int]) =
        if pos notin group:
          boundary.incl(pos)

      incl(up)
      incl(down)
      incl(left)
      incl(right)

    var t = 0
    for point in group:
      let r = point + newVector(0, 1)
      let u = point + newVector(-1, 0)
      let l = point + newVector(0, -1)
      let d = point + newVector(1, 0)

      let ru = point + newVector(-1, 1)
      let ld = point + newVector(1, -1)
      let rd = point + newVector(1, 1)
      let lu = point + newVector(-1, -1)

      if r in boundary and u in boundary:
        t += 1
      if r notin boundary and u notin boundary and ru in boundary:
        t += 1

      if r in boundary and d in boundary:
        t += 1
      if r notin boundary and d notin boundary and rd in boundary:
        t += 1

      if l in boundary and d in boundary:
        t += 1
      if l notin boundary and d notin boundary and ld in boundary:
        t += 1

      if l in boundary and u in boundary:
        t += 1
      if l notin boundary and u notin boundary and lu in boundary:
        t += 1

    s += t * group.len

  echo s
