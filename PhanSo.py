from math import gcd

class MauSoBangKhong(Exception):
    def __init__(self, mau_so):
        self.mau_so = mau_so
        super().__init__(f"mau so '{mau_so}' khong hop le (phai khac 0)")

class PhanSo:
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so

    @property
    def tu_so(self):
        return self.__tu

    @tu_so.setter
    def tu_so(self, value):
        self.__tu = value

    @property
    def mau_so(self):   
        return self.__mau

    @mau_so.setter
    def mau_so(self, value):
        if value == 0:
            raise MauSoBangKhong(value)
        self.__mau = value

    def toi_gian(self):
        g = gcd(abs(self.__tu), abs(self.__mau))
        tu  = self.__tu  // g
        mau = self.__mau // g
        if mau < 0:
            tu, mau = -tu, -mau
        return PhanSo(tu, mau)

    def is_toi_gian(self):
        return gcd(abs(self.__tu), abs(self.__mau)) == 1

    def __add__(self, other):
        tu  = self.__tu * other.__mau + other.__tu * self.__mau
        mau = self.__mau * other.__mau
        return PhanSo(tu, mau).toi_gian()

    def __sub__(self, other):
        tu  = self.__tu * other.__mau - other.__tu * self.__mau
        mau = self.__mau * other.__mau
        return PhanSo(tu, mau).toi_gian()

    def __mul__(self, other):
        return PhanSo(
            self.__tu * other.__tu,
            self.__mau * other.__mau
        ).toi_gian()

    def __truediv__(self, other):
        if other.__tu == 0:
            raise ZeroDivisionError("Chia cho phan so co tu = 0")
        return PhanSo(
            self.__tu * other.__mau,
            self.__mau * other.__tu
        ).toi_gian()

    def __eq__(self, other):
        a = self.toi_gian()
        b = other.toi_gian()
        return a.__tu == b.__tu and a.__mau == b.__mau

    def __lt__(self, other):
        return self.__tu * other.__mau < other.__tu * self.__mau

    def __gt__(self, other):
        return self.__tu * other.__mau > other.__tu * self.__mau

    def __hash__(self):
        r = self.toi_gian()
        return hash((r.__tu, r.__mau))

    def __str__(self):
        if self.__mau == 1:
            return str(self.__tu)
        return f"{self.__tu}/{self.__mau}"

    def __repr__(self):
        return f"PhanSo({self.__tu}, {self.__mau})"

ds = [PhanSo(2, 4), PhanSo(3, 6), PhanSo(1, 3), PhanSo(5, 7)]

print("-- Day phan so & dang toi gian --")
for ps in ds:
    tg = ps.toi_gian()
    print(f"  {ps} -> toi gian: {tg}  (da TG? {ps.is_toi_gian()})")

print("\n-- Phep toan --")
ps_a = PhanSo(1, 3)
ps_b = PhanSo(5, 7)
print(f"  {ps_a} + {ps_b} = {ps_a + ps_b}")
print(f"  {ps_a} - {ps_b} = {ps_a - ps_b}")
print(f"  {ps_a} * {ps_b} = {ps_a * ps_b}")
print(f"  {ps_a} / {ps_b} = {ps_a / ps_b}")

print("\n-- Sap xep tang dan --")
for ps in sorted(ds):
    tg = ps.toi_gian()
    print(f"  {tg} = {ps.tu_so/ps.mau_so:.4f}")

print("\n-- So sanh --")
print(f"  2/4 == 3/6 ? {PhanSo(2,4) == PhanSo(3,6)}")
print(f"  1/3 < 5/7  ? {ps_a < ps_b}")
print(f"  5/7 > 1/3  ? {ps_b > ps_a}")

print("\n-- Loai trung (set) --")
ds2 = [PhanSo(1,2), PhanSo(2,4), PhanSo(3,6)]
unique = list(set(ds2))
print(f"  Truoc: {[str(p) for p in ds2]}")
print(f"  Sau set: {[str(p) for p in unique]}")

print("\n-- Validation --")
try:
    ps_loi = PhanSo(5, 0)
except MauSoBangKhong as e:
    print(f"  Bat loi: {e}")
