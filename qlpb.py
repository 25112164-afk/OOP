LUONG_CO_BAN = 5_000_000

class NhanVien:
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh,
                 dia_chi, he_so_luong, luong_toi_da):
        self._ma_nv       = ma_nv
        self._ho_ten      = ho_ten
        self._nam_sinh    = nam_sinh
        self._gioi_tinh   = gioi_tinh
        self._dia_chi     = dia_chi
        self._he_so_luong = he_so_luong if he_so_luong > 0 else 1.0
        self._luong_toi_da = luong_toi_da

    def tinh_luong(self):
        return LUONG_CO_BAN * self._he_so_luong

    def hien_thi(self):
        print(f"  Mã NV     : {self._ma_nv}")
        print(f"  Họ tên    : {self._ho_ten}")
        print(f"  Năm sinh  : {self._nam_sinh}")
        print(f"  Giới tính : {self._gioi_tinh}")
        print(f"  Địa chỉ   : {self._dia_chi}")
        print(f"  Hệ số     : {self._he_so_luong}")
        print(f"  Lương      : {self.tinh_luong():,.0f} VNĐ")


class CongTacVien(NhanVien):
    HD_HOP_LE = ["3 tháng", "6 tháng", "1 năm"]

    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh,
                 dia_chi, he_so_luong, luong_toi_da,
                 thoi_han_hd, phu_cap_ld):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh,
                         dia_chi, he_so_luong, luong_toi_da)
        if thoi_han_hd not in CongTacVien.HD_HOP_LE:
            raise ValueError(f"Thời hạn HĐ phải là: {CongTacVien.HD_HOP_LE}")
        self.__thoi_han_hd = thoi_han_hd
        self.__phu_cap_ld  = phu_cap_ld

    def tinh_luong(self):
        return super().tinh_luong() + self.__phu_cap_ld

    def hien_thi(self):
        print("═══ CỘNG TÁC VIÊN ═══")
        super().hien_thi()
        print(f"  Thời hạn HĐ: {self.__thoi_han_hd}")
        print(f"  Phụ cấp LĐ : {self.__phu_cap_ld:,.0f} VNĐ")


class NVChinhThuc(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh,
                 dia_chi, he_so_luong, luong_toi_da, vi_tri):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh,
                         dia_chi, he_so_luong, luong_toi_da)
        self.__vi_tri = vi_tri

    def hien_thi(self):
        print("═══ NHÂN VIÊN CHÍNH THỨC ═══")
        super().hien_thi()
        print(f"  Vị trí    : {self.__vi_tri}")


class TruongPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh,
                 dia_chi, he_so_luong, luong_toi_da,
                 ngay_bat_dau_ql, phu_cap_ql):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh,
                         dia_chi, he_so_luong, luong_toi_da)
        self.__ngay_bat_dau_ql = ngay_bat_dau_ql
        self.__phu_cap_ql      = phu_cap_ql

    def tinh_luong(self):
        return super().tinh_luong() + self.__phu_cap_ql

    def hien_thi(self):
        print("═══ TRƯỞNG PHÒNG ═══")
        super().hien_thi()
        print(f"  Ngày BĐ QL: {self.__ngay_bat_dau_ql}")
        print(f"  Phụ cấp QL: {self.__phu_cap_ql:,.0f} VNĐ")


ctv = CongTacVien(
    "CTV01", "Trần Thị B", 2000, "Nữ", "Hà Nội",
    1.5, 30_000_000,
    "6 tháng", 1_500_000
)

nvct = NVChinhThuc(
    "NV01", "Lê Văn C", 1995, "Nam", "Đà Nẵng",
    2.0, 40_000_000,
    "Kỹ sư phần mềm"
)

tp = TruongPhong(
    "TP01", "Nguyễn Văn D", 1985, "Nam", "TP.HCM",
    3.0, 50_000_000,
    "01/01/2020", 5_000_000
)

ctv.hien_thi()
print()
nvct.hien_thi()
print()
tp.hien_thi()

print("\n══ BẢNG LƯƠNG PHÒNG BAN (Polymorphism) ══")
ds_nv = [ctv, nvct, tp]
for nv in ds_nv:
    print(f"  {nv._ho_ten:<20s} → {nv.tinh_luong():>12,.0f} VNĐ")