import math
class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    def hien_thi(self):
        print(f"({self.x}, {self.y})")

print("--- YÊU CẦU 1 & 2 ---")
A = Point(3, 4)
print("Tọa độ điểm A: ", end="")
A.hien_thi()

bx = int(input("Nhập tọa độ x cho điểm B: "))
by = int(input("Nhập tọa độ y cho điểm B: "))
B = Point(bx, by)
print("Tọa độ điểm B: ", end="")
B.hien_thi()

print("\n--- YÊU CẦU 3 ---")
C = Point(-B.x, -B.y)
print("Tọa độ điểm C (đối xứng B qua O): ", end="")
C.hien_thi()

print("\n--- YÊU CẦU 4 & 5 ---")

khoang_cach_B_O = math.sqrt(B.x**2 + B.y**2)
print(f"Khoảng cách từ B đến O: {khoang_cach_B_O}")

khoang_cach_A_B = math.sqrt((A.x - B.x)**2 + (A.y - B.y)**2)
print(f"Khoảng cách từ A đến B: {khoang_cach_A_B}")