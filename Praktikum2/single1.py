class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def berbunyi(self):
        print("Burung",self.nama, "Berbunyi")
        

class Burung(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu
    def bersuara(self):
        print("Merdu")
        print("berumur", self.umur, "tahun")

BirdA = Burung("Kaka Tua", 1, "Merdu")
BirdA.berbunyi() 
BirdA.bersuara()