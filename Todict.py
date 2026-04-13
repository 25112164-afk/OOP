import json
class CongNhan:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi  
    def to_dict(self):
        return{
            "ho_ten":       self.ho_ten,
            "tuoi":         self.tuoi,
            "gioi_tinh":    self.gioi_tinh,
            "dia_chi":      self.dia_chi,
            "loai":    self.__class__.__name__,
        }

class Canbo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi  
    def to_dict(self):
        return{
            "ho_ten":       self.ho_ten,
            "tuoi":         self.tuoi,
            "gioi_tinh":    self.gioi_tinh,
            "dia_chi":      self.dia_chi,
            "loai":    self.__class__.__name__,
        }
    @classmethod
    def from_dict(cls, d):
        return cls(d["ho_ten"], d["tuoi"], d["gioi_tinh"], d["dia_chi"])
danh_sach = [
    Canbo("Nguyen Kien", 18, "Nam", "Ha Noi"),
    CongNhan("Le Nam", 20, "Nam", "Hoa Lac")
]

data = [cb.to_dict() for cb in danh_sach]

with open ("canbo.json", "w",
           encoding="utf-8") as f:

     json.dump(data, f,
               ensure_ascii=False, indent=2)
     
with open ("canbo.json", "r",
           encoding="utf-8") as f:

     raw = json.load(f)
    
ds_loaded = [Canbo.from_dict(d)
             for d in raw]
for cb in ds_loaded:
    print(cb)