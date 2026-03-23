
class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac
danh_sach = [] 
print("--- BẮT ĐẦU NHẬP SIÊU NHÂN ---")
while True:
    ten_nhap = input("Nhập tên siêu nhân (hoặc gõ 'q' để dừng lại): ")
    
    if ten_nhap.lower() == 'q':
        break
        
    vu_khi_nhap = input("Nhập vũ khí: ")
    mau_sac_nhap = input("Nhập màu sắc: ")
    
    sn_moi = SieuNhan(ten_nhap, vu_khi_nhap, mau_sac_nhap)
    danh_sach.append(sn_moi)
    print("-> Đã thêm thành công!\n")
print("\n=== DANH SÁCH SIÊU NHÂN TOÀN THẾ GIỚI ===")
for sn in danh_sach:
    print(f"Tên: {sn.ten} | Vũ khí: {sn.vu_khi} | Màu sắc: {sn.mau_sac}")