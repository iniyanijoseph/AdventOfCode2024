type Vector*[T] = object
  x*: T
  y*: T

# type Vector*[T] = tuple[x: T, y: T]

proc newVector*[T](x, y : T): Vector[T] =
  return Vector[T](x:x, y:y)

proc `+`*[T](a, b : Vector[T]): Vector[T] =
  return Vector[T](x: a.x + b.x, y: a.y+b.y)

proc `-`*[T](a, b : Vector[T]): Vector[T] =
  return Vector[T](x: a.x - b.x, y: a.y - b.y)

proc `*`*[T](a : T, b: Vector[T]) : Vector[T] =
  return Vector[T](x : a*b.x, y: a*b.y)
proc `*`*[T](a : Vector[T], b : T) : Vector[T] =
  return Vector[T](x : a.x*b,y: a.y*b)

proc `*`*[T](a:Vector[T], b:Vector[T]) : T =
  return a.x*b.x + a.y*b.y

proc `==`*[T](a:Vector[T], b:Vector[T]) : bool =
  return a.x == b.x and a.y == b.y

