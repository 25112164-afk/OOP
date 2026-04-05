class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_sx):
        self.__ma_hang  = ma_hang
        self.__ten_hang = ten_hang
        self.__nha_sx   = nha_sx

    def getMaHang(self):   return self.__ma_hang
    def getTenHang(self):  return self.__ten_hang
    def getNhaSX(self):    return self.__nha_sx

    def hien_thi(self):
        print(f"  Mã hàng  : {self.__ma_hang}")
        print(f"  Tên hàng : {self.__ten_hang}")
        print(f"  Nhà SX   : {self.__nha_sx}")


class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_baohanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx)
        self.__gia        = gia
        self.__tg_baohanh = tg_baohanh
        self.__dien_ap    = dien_ap
        self.__cong_suat  = cong_suat

    def hien_thi(self):
        print("═══ HÀNG ĐIỆN MÁY ═══")
        super().hien_thi()
        print(f"  Giá      : {self.__gia:,.0f} VNĐ")
        print(f"  Bảo hành : {self.__tg_baohanh} tháng")
        print(f"  Điện áp  : {self.__dien_ap} V")
        print(f"  Công suất: {self.__cong_suat} W")


class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyen_lieu):
        super().__init__(ma_hang, ten_hang, nha_sx)
        self.__gia              = gia
        self.__loai_nguyen_lieu = loai_nguyen_lieu

    def hien_thi(self):
        print("═══ HÀNG SÀNH SỨ ═══")
        super().hien_thi()
        print(f"  Giá         : {self.__gia:,.0f} VNĐ")
        print(f"  Nguyên liệu : {self.__loai_nguyen_lieu}")


class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_het_han):
        super().__init__(ma_hang, ten_hang, nha_sx)
        self.__gia         = gia
        self.__ngay_sx     = ngay_sx
        self.__ngay_het_han = ngay_het_han

    def hien_thi(self):
        print("═══ HÀNG THỰC PHẨM ═══")
        super().hien_thi()
        print(f"  Giá        : {self.__gia:,.0f} VNĐ")
        print(f"  Ngày SX    : {self.__ngay_sx}")
        print(f"  Hết hạn    : {self.__ngay_het_han}")


dm = HangDienMay(
    "DM001", "Tủ lạnh Inverter 360L", "Samsung",
    12_500_000, 24, 220, 150
)

ss = HangSanhSu(
    "SS001", "Bộ chén sứ Minh Long", "Minh Long",
    850_000, "Sứ cao cấp"
)

tp = HangThucPham(
    "TP001", "Cà phê rang xay Aura Brew", "Aura Brew",
    185_000, "01/03/2026", "01/03/2027"
)

dm.hien_thi()
print()
ss.hien_thi()
print()
tp.hien_thi()