import algorithm, sequtils, sugar, strutils, tables, lib/vector, re, pegs, math, lenientops

var inp = collect:
  for line in lines("13.txt"):
    if line != "":
      line

proc isInteger(n: float): bool = n.round().almostEqual(n, 10)

block:
  var x : seq[array[2, array[3, float64]]] = @[]
  var current : array[2, array[3, float64]]
  for i, line in inp.pairs:
    var vals = map(split(line, peg"\D*"), (x)=>parseInt(x))
    current[0][i mod 3] = float64(vals[0])
    current[1][i mod 3] = float64(vals[1])
    if i mod 3 == 2:
      x.add(current)
  var s = 0
  for i, arr in x.pairs:
    let c = -arr[0][0]/arr[1][0]
    let bp = c*arr[1][1]+arr[0][1]
    let k = c*arr[1][2]+arr[0][2]
    let b = k/bp
    let a = (arr[0][2]-b*arr[0][1])/arr[0][0]

    if isInteger(a) and isInteger(b):
      if a >= 0 and b >= 0 and a <= 100 and b <= 100:
        s += 3*int(round(a)) + int(round(b))
    # else:
    #   echo a, "\t", b

  echo s

block:
  var x : seq[array[2, array[3, float64]]] = @[]
  var current : array[2, array[3, float64]]
  for i, line in inp.pairs:
    var vals = map(split(line, peg"\D*"), (x)=>parseInt(x))
    current[0][i mod 3] = float64(vals[0])
    current[1][i mod 3] = float64(vals[1])
    if i mod 3 == 2:
      current[0][i mod 3] += 10000000000000.0
      current[1][i mod 3] += 10000000000000.0
      x.add(current)

  var s = 0
  for i, arr in x.pairs:
    let c = -arr[0][0]/arr[1][0]
    let bp = c*arr[1][1]+arr[0][1]
    let k = c*(arr[1][2])+(arr[0][2])
    let b = k/bp
    let a = ((arr[0][2])-b*arr[0][1])/arr[0][0]

    if isInteger(a) and isInteger(b):
      if a >= 0 and b >= 0:
        s += 3*int(round(a)) + int(round(b))
    # else:
    #   echo a, "\t", b
  echo s
