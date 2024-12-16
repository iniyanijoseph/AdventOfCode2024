import sequtils, strutils, tables, lib/vector, sugar, tables, math, std/strformat
import progress

var inp =
  block:
    var i = collect:
      for line in lines("11.txt"):
        map(line.split(" "), (x)=>parseInt(x), )
    i[0]


var dp = initTable[(int, int, int), int]()
proc blink(i : int) : seq[int] =
  if i == 0:
    return @[1]

  var numLength = int(floor(log10(float(i)))+1)

  if numLength mod 2 == 0:
    var half : int = int(numLength / 2)

    return @[parseInt(($i)[0..(half-1)]), parseInt(($i)[half..^1])]

  return @[i*2024]

proc run(i : int, depth : int, target : int) : int =
  if depth == target:
    return 1

  if (i, depth, target) in dp:
    return dp[(i, depth, target)]

  var blinked = blink(i)

  var s = 0
  for k in blinked:
    s += run(k, depth+1, target)

  dp[(i, depth, target)] = s

  return s

var s = 0

for i in inp:
  s += run(i, 0, 25)

echo s

s = 0

for i in inp:
  s += run(i, 0, 75)

echo s

