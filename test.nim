import sets


var r = initHashSet[int]()

proc y (a: int, x: HashSet[int]) =
  x.incl(a)

y(4, r)

echo x
