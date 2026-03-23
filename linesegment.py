from point import Point
import copy

class LineSegment:
    def __init__(self, *args):
        if len(args)==0:
            self._d1 = Point(8,5)
            self._d2 = Point(1,0)
        if len(args)==2:
            if isinstance(args[0], Point) and isinstance(args[1], Point):
                self._d1 = args[0]
                self._d2 = args[1]
        if len(args)==4:
            if isinstance(args[0], int) and isinstance(args[1], int) and isinstance(args[2], int) and isinstance(args[3], int):
                self._d1 = Point(args[0], args[1])
                self._d2 = Point(args[2], args[3])
        if len(args)==1:
            if isinstance(args[0], LineSegment):
                self._d1 = copy.deepcopy(args[0]._d1)
                self._d2 = copy.deepcopy(args[0]._d2)
    def __str__(self):
        return "[(%d,%d),(%d,%d)]" % (self._d1.x,self._d1.y,self._d2.x,self._d2.y) 
    
    def getD1(self):
        return self._d1

    def getD2(self):
        return self._d2
    def getD1D2(self,point1,point2):
        self.d1_ =point1
        self.d2_ =point2

if __name__ == "__main__":

    l1 = LineSegment()
    print(l1)

    p1 = Point(3,4)
    p2 = Point(5,6)
    l2 = LineSegment(p1,p2)
    print(l2)

    l3 = LineSegment(-3,-4,-5,-6)
    print(l3)

    l4 = LineSegment(l2)
    print(l4)
    
    print(l1.getD1())
    print(l1.getD2())                   