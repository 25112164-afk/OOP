from point import Point
import copy

class LineSegment:
    def __init__(self, *args):
        if len(args) == 0:
            self._d1 = Point(8, 5)
            self._d2 = Point(1, 0)
        
        elif len(args) == 1 and isinstance(args[0], LineSegment):
            self._d1 = copy.deepcopy(args[0]._d1)
            self._d2 = copy.deepcopy(args[0]._d2)
            
        elif len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):
            self._d1 = args[0]
            self._d2 = args[1]
            
        elif len(args) == 4:
            self._d1 = Point(args[0], args[1])
            self._d2 = Point(args[2], args[3])

    def __str__(self):
        return "[(%d,%d),(%d,%d)]" % (self._d1.x, self._d1.y, self._d2.x, self._d2.y) 
    
    def getD1(self):
        return self._d1

    def getD2(self):
        return self._d2

if __name__ == "__main__":
    l1 = LineSegment()
    print(l1)

    p1 = Point(3, 4)
    p2 = Point(5, 6)
    l2 = LineSegment(p1, p2)
    print(l2)

    l3 = LineSegment(-3, -4, -5, -6)
    print(l3)

    l4 = LineSegment(l2)
    print(l4)                   