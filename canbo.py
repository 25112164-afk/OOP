class Canbo:
    def __init__(self, hoten, tuoi, gioitinh, diachi):
        self._hoten = hoten
        self._tuoi = tuoi
        self._gioitinh = gioitinh
        self._diachi = diachi
        
    def loai_cb(self):
        return "Cán bộ"
    
    def hien_thi_cb(self):
        print(f"[{self.loai_cb()}] Họ tên: {self._hoten}, Tuổi: {self._tuoi}, Giới tính: {self._gioitinh}, Địa chỉ: {self._diachi}")

class CongNhan(Canbo):
    def __init__(self, hoten, tuoi, gioitinh, diachi, bac): 
        super().__init__(hoten, tuoi, gioitinh, diachi)
        self._bac = bac  
        
    def loai_cb(self):
        return "Công nhân"
    
    def hien_thi_cb(self):

        super().hien_thi_cb()

        print(f" -> Bậc: {self._bac}")

class Kysu(Canbo):
    def __init__(self, hoten, tuoi, gioitinh, diachi, nganh): 
        super().__init__(hoten, tuoi, gioitinh, diachi)
        self._nganh = nganh  
        
    def loai_cb(self):
        return "Kỹ sư"
    
    def hien_thi_cb(self):

        super().hien_thi_cb()

        print(f" -> Ngành: {self._nganh}")

class NhanVien(Canbo):
    def __init__(self, hoten, tuoi, gioitinh, diachi, congviec): 
        super().__init__(hoten, tuoi, gioitinh, diachi)
        self._congviec = congviec  
        
    def loai_cb(self):
        return "Nhân viên"
    
    def hien_thi_cb(self):

        super().hien_thi_cb()

        print(f" -> Công việc: {self._congviec}")
cb1 = Canbo("Kien", 30, "Nam", "Ham Nghi")
cb2 = CongNhan("Nam", 35, "Nam", "Hoa Lac", 5)
cb3 = Kysu("Minh", 40, "Nam", "Dong Da", "Công nghệ thông tin")
cb4 = NhanVien("Lan", 28, "Nữ", "Ba Đình", "Marketing")

cb1.hien_thi_cb()
cb2.hien_thi_cb()
cb3.hien_thi_cb()
cb4.hien_thi_cb()