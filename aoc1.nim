import algorithm, sequtils, sugar, strutils, tables

var a : seq[int] = @[]
var b : seq[int] = @[]

for line in lines("1.txt"):
  var splitLine = line.split("   ")
  a.add(parseInt(splitLine[0]))
  b.add(parseInt(splitLine[1]))

a.sort()
b.sort()

var result = 0
for i in 0..<len(a):
  result += abs(a[i]-b[i])

echo result

result = 0

var bCount = initCountTable[int]()
for i in b:
  bCount.inc(i)

for i in a:
  result += i*bCount[i]

echo result



