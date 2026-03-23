import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def point_in_circle(circle, point):
    return distance(circle.center, point) <= circle.radius

def lay_4_goc_hcn(rect):
    p1 = rect.corner
    p2 = Point(rect.corner.x + rect.width, rect.corner.y)
    p3 = Point(rect.corner.x, rect.corner.y + rect.height)
    p4 = Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
    
    danh_sach_goc = [p1, p2, p3, p4]
    return danh_sach_goc

def rect_in_circle(circle, rect):
    danh_sach_goc = lay_4_goc_hcn(rect)
    
    for goc in danh_sach_goc:
        if point_in_circle(circle, goc) == False:
            return False 
            
    return True 

def rect_circle_overlap(circle, rect):
    danh_sach_goc = lay_4_goc_hcn(rect)
    
    for goc in danh_sach_goc:
        if point_in_circle(circle, goc) == True:
            return True 
            
    return False 

tam_hinh_tron = Point(150, 100)
vong_tron = Circle(tam_hinh_tron, 75)

hcn_to = Rectangle(Point(100, 50), 200, 200)

print(f"HCN to nằm trọn trong vòng tròn? -> {rect_in_circle(vong_tron, hcn_to)}")
print(f"HCN to có chạm vào vòng tròn không? -> {rect_circle_overlap(vong_tron, hcn_to)}")