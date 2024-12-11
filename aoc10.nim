import strutils, sequtils, sugar, sets, lib/vector, tables

let inp = collect:
  for line in lines("10.txt"):
    map(line, (x)=>ord(x)-ord('0'))

#[
var points : HashSet[Vector[int]]

proc findTrail(x : int, y : int, current : int, grid : seq[seq[int]]) =
  if not (0 <= x and x < grid.len) or not (0 <= y and y < grid[0].len):
    return
  if grid[x][y] != current:
    return
  elif grid[x][y] == 9:
    points.incl(newVector(x, y))

  findTrail(x+1,y,current+1, grid)
  findTrail(x-1,y,current+1, grid)
  findTrail(x,y+1,current+1, grid)
  findTrail(x,y-1,current+1, grid)

var s = 0
for i in 0..<inp.len:
  for j in 0..<inp[0].len:
    if inp[i][j] == 0:
      points = initHashSet[Vector[int]]()
      findTrail(i, j, 0, inp)
      s += points.len

echo s
]#


var points = initTable[Vector[int], int]()

proc findTrail(x : int, y : int, current : int, grid : seq[seq[int]]) =
  if not (0 <= x and x < grid.len) or not (0 <= y and y < grid[0].len):
    return
  if grid[x][y] != current:
    return
  elif grid[x][y] == 9:
    let point = newVector(x, y)
    if point notin points:
      points[point] = 0
    points[point] += 1

  findTrail(x+1,y,current+1, grid)
  findTrail(x-1,y,current+1, grid)
  findTrail(x,y+1,current+1, grid)
  findTrail(x,y-1,current+1, grid)

var s = 0
for i in 0..<inp.len:
  for j in 0..<inp[0].len:
    if inp[i][j] == 0:
      points = initTable[Vector[int], int]()
      findTrail(i, j, 0, inp)
      for point, count in points.pairs:
        s += count


echo s
