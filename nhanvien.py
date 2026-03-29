class NhanVien:
    LUONG_MAX = 50_000_000

    def __init__(self, ten_nhan_vien, luong_co_ban, he_so_luong):
        self.__tenNhanVien = ten_nhan_vien
        self.__luongCoBan  = luong_co_ban
        self.__heSoLuong   = he_so_luong

    def getTenNhanVien(self):
        return self.__tenNhanVien

    def getLuongCoBan(self):
        return self.__luongCoBan

    def getHeSoLuong(self):
        return self.__heSoLuong

    def setTenNhanVien(self, value):
        self.__tenNhanVien = value

    def setLuongCoBan(self, value):
        if value < 0:
            print("Lương cơ bản không được âm!")
            return
        self.__luongCoBan = value

    def setHeSoLuong(self, value):
        if value <= 0:
            print("Hệ số lương phải lớn hơn 0!")
            return
        self.__heSoLuong = value

    def tinhLuong(self):
        return self.__luongCoBan * self.__heSoLuong

    def inTTin(self):
        luong = self.tinhLuong()
        print("========== THÔNG TIN NHÂN VIÊN ==========")
        print(f"  Tên NV   : {self.__tenNhanVien}")
        print(f"  Lương CB : {self.__luongCoBan:,.0f} VNĐ")
        print(f"  Hệ số    : {self.__heSoLuong}")
        print(f"  Lương TT : {luong:,.0f} VNĐ")
        print("==========================================")

    def tangLuong(self, delta):
        he_so_moi = self.__heSoLuong + delta
        luong_moi = self.__luongCoBan * he_so_moi
        if luong_moi > NhanVien.LUONG_MAX:
            print(f"Lương mới ({luong_moi:,.0f}) vượt LUONG_MAX ({NhanVien.LUONG_MAX:,.0f}). Không tăng!")
            return False
        self.__heSoLuong = he_so_moi
        print(f"Đã tăng hệ số lương! Lương mới: {self.tinhLuong():,.0f} VNĐ")
        return True

if __name__ == "__main__":
    nv = NhanVien("Nguyễn Văn A", 10_000_000, 2.0)
    nv.inTTin()
    
    print("\n--- Test tangLuong ---")
    nv.tangLuong(0.5)
    nv.inTTin()
    nv.tangLuong(3.0)

    print("\n--- Test getter/setter ---")
    print(f"Tên: {nv.getTenNhanVien()}")
    nv.setLuongCoBan(12_000_000)
    print(f"Lương CB mới: {nv.getLuongCoBan():,.0f}")
    print(f"Lương TT mới: {nv.tinhLuong():,.0f}")