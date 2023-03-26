print("Lais Cakrawati\n210511002\nTI21A\n")

class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bergerak(self):
        print(self.nama, "bergerak")

class Kucing(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu

    def bersuara(self):
        print("Meow!")

kucingA = Kucing("moca", 2, "anggora")
kucingA.bergerak() # output: moca bergerak
kucingA.bersuara() # output: Meow!
