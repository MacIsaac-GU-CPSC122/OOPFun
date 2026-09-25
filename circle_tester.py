import copy

class Point:
    def __init__(self, x:float = 0, y:float = 0) -> None:
        self._x = x
        self._y = y

    def __str__(self) -> str:
        return f"({self._x}, {self._y})"

    def update_x(self, x:float):
        if x < 0:
            print("ERROR: must be positive")
        self._x = x

class Circle:
    def __init__(self, radius:float = 0, point:Point = None) -> None:
        if point == None:
            point = Point()
        self._center = point
        self._radius = radius

    def __str__(self) -> str:
        return f"Circle with radius {self._radius} at {self._center}"

    def update_radius(self, radius:float) -> None:
        self._radius = radius

p1 = Point()
p2 = Point(2,3)
print(p1)
print(p2)
c1 = Circle()
print(c1)
c2 = Circle(4, p2)
print(p2)
print(c2)

c2_deep_copy = copy.deepcopy(c2)
c2_shallow = copy.copy(c2)
c2_alias = c2
p2.update_x(1000)
c2.update_radius(3000)
print("c2", c2)
print("c2_deep", c2_deep_copy)
print("c2_shallow", c2_shallow)
print("c2_alias", c2_alias)

