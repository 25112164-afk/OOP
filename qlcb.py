from canbo import CongNhan, Kysu, NhanVien

class QLCB:
    def __init__(self):
        self._danhsach = []

    def themmoi(self):
        print("Nhập vào công nhân (1), kỹ sư (2) hay nhân viên (3)?")
        loai = input("")
        hoten = input("Nhập vào họ và tên: ")
        tuoi = input("Nhập vào tuổi: ")
        gioitinh = input("Nhập vào giới tính: ")
        diachi = input("Nhập vào địa chỉ: ")
        
        if loai == "1":
            bac = input("Nhập vào Bậc Công Nhân: ")
            cb = CongNhan(hoten, tuoi, gioitinh, diachi, bac)
        elif loai == "2":
            nganh = input("Nhập vào Ngành Kỹ Sư: ")
            cb = Kysu(hoten, tuoi, gioitinh, diachi, nganh)

        elif loai == "3":
            congviec = input("Nhập vào Công Việc Nhân Viên: ")
            cb = NhanVien(hoten, tuoi, gioitinh, diachi, congviec)
            
        self._danhsach.append(cb)
        print(f"  ✓ Đã thêm: {cb}")
    def timkiem(self):
        ten = input("Nhập vào tên cần tìm: ")
        for cb in self._danhsach:
            if cb._hoten == ten:
                cb.hien_thi_cb()

       
    def hienthi(self):
        for cb in self._danhsach:
            cb.hien_thi_cb()
    def chay(self):
        while True:
            print("nhập loại yêu cầu")
            print("1. Thêm mới cán bộ")
            print("2. Tìm kiếm theo họ tên")
            print("3. Hiển thị thông tin về danh sách các cán bộ")
            print("4. Thoát khỏi chương trình")
            loai = input("")
            if loai == "1":
                self.themmoi()
            elif loai == "2":
                self.timkiem()
            elif loai == "3":
                self.hienthi()
            elif loai == "4":
                break
if __name__ == "__main__":
    qlcb = QLCB()
    qlcb.chay()