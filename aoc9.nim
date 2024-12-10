import strutils, sequtils, sugar, tables, sets, macros, algorithm
import lib/vector


# Weighted Graph
var inp : seq[int] = @[]
for line in lines("9.txt"):
  inp = @line.map((x)=>ord(x)-ord('0'))

var line : seq[int] = @[]
var freeSpaceStarts : seq[int] = @[]
var freeSpace : seq[int] = @[]

var count = 0
for i, e in inp.pairs:
  if i mod 2 == 0:
    for j in 0..<e:
      line.add(count)
    count += 1
  else:
    freeSpace.add(e)
    freeSpaceStarts.add(line.len)
    for j in 0..<e:
      line.add(-1)


#Part 1
var i = 0
var j = line.len - 1

var s = 0
while(i <= j):
  if line[i] != -1:
    s += line[i] * i
  else:
    while line[j] == -1:
      j-=1
    if i > j:
      break
    s += line[j] * i
    j -= 1
  i += 1

echo s



#Part 2
j = line.len - 1
count -= 1

while line[j] != count:
    j -= 1

while(count > 0):
  var num = 0
  while line[j-num] == count:
    num += 1

  j -= num

  for i in 0..<freeSpace.len:
    if num <= freeSpace[i] and freeSpaceStarts[i] < j:
      for k in 0..<num:
        line[freeSpaceStarts[i]+k] = count
        line[j+k+1] = -1

      freeSpace[i] -= num
      freeSpaceStarts[i] += num
      break;

  count-=1
  while line[j] != count:
    j -= 1

s = 0
for i, e in line.pairs:
  if e != -1:
    s += i*e

echo s

