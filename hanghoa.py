from abc import ABC, abstractmethod
class GiaKhongHopLe(Exception):
    def __init__(self, gia):
        self._gia = gia
        super().__init__(f"Gia '{gia}' khong hop le (phai >= 0)")

class HangHoa(ABC):
    def __init__(self, ma_hang, ten_hang, nha_sx):
        self.__ma_hang  = ma_hang
        self.__ten_hang = ten_hang
        self.__nha_sx   = nha_sx
    @property
    def ma_hang(self):
        return self.__ma_hang
    @property
    def ten_hang(self):
        return self.__ten_hang
    @property
    def nha_sx(self):
        return self.__nha_sx
  
    @abstractmethod
    def loai_hang(self):
        pass
    
    def inTTin(self):
            return(f"[{self.loai_hang()}] {self.ma_hang} - {self.ten_hang} ({self.nha_sx})")
    
    def __str__(self):
        return self.inTTin()

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.__ma_hang}', "
                f"'{self.__ten_hang}', '{self.__nha_sx}', {self._gia})")

    def __eq__(self, other):
        if not isinstance(other, HangHoa): return NotImplemented
        return self.__ma_hang == other.__ma_hang

    def __lt__(self, other):
        return self._gia < other._gia

    def __hash__(self):
        return hash(self.__ma_hang)



class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_baohanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx)
        self._gia        = gia
        self.__tg_baohanh = tg_baohanh
        self._dien_ap    = dien_ap
        self._cong_suat  = cong_suat
    def loai_hang(self):
        return "dien may"
    
    def inTTin(self):
        return(f"{super().inTTin()} | BH: {self.__tg_baohanh}th"
               f" | {self._dien_ap}V | {self._cong_suat}W")


class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyen_lieu):
        super().__init__(ma_hang, ten_hang, nha_sx)
        self._gia              = gia
        self.__loai_nguyen_lieu = loai_nguyen_lieu

    def loai_hang(self):
        return "sanh su"
    
    def inTTin(self):
        return (f"{super().inTTin()} | {self.__loai_nguyen_lieu}")
    


class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_het_han):
        super().__init__(ma_hang, ten_hang, nha_sx)
        self._gia         = gia
        self.__ngay_sx     = ngay_sx
        self.__ngay_het_han = ngay_het_han
    def loai_hang(self):
        return "thuc pham"
    def inTTin(self):
        return (f"{super().inTTin()} | NSX: {self.__ngay_sx} | HSD: {self.__ngay_het_han}")
    
sp1 = HangDienMay("HAIBZK1", "Fridge", "MEHAI", 12_000_000, 24, 220, 150)
sp2 = HangSanhSu("BIMBIMBAMBAMBUMBUM", "Binh hoa", "MEBIN", 350_000, "su cao cap")
sp3 = HangThucPham("LILI2", "Sữa tươi", "Vinamilk", 32_000, "2025-01-01", "2025-07-01")

print("── Đa hình: print(sp) ──")
kho = [sp1, sp2, sp3]
for sp in kho:
    print(sp)          

print("\n── Sắp xếp theo giá ──")
for sp in sorted(kho):
    print(f"  {sp._gia:>12,.0f}đ | {sp.ten_hang}")

print("\n── So sánh & loại trùng ──")
sp1_copy = HangDienMay("DM01", "Tủ lạnh", "LG", 12_000_000, 24, 220, 150)
print(f"  sp1 == sp1_copy? {sp1 == sp1_copy}")
print(f"  set loại trùng: {len([sp1, sp2, sp1_copy])} → {len(set([sp1, sp2, sp1_copy]))}")

print("\n── Validation ──")
try:
    sp_loi = HangDienMay("DM99", "Test", "X", -5000, 12, 220, 50)
except GiaKhongHopLe as e:
    print(f"  Bắt lỗi: {e}")

try:
    h = HangHoa("X", "Test", "Y", 100)
except TypeError as e:
    print(f"  ABC: {e}")

print("\n── Lưu file (with) ──")
with open("kho_hang.txt", "w", encoding="utf-8") as f:
    for sp in kho:
        f.write(repr(sp) + "\n")
print(f"  Đã lưu {len(kho)} sản phẩm")