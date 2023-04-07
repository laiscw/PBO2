class Pekerja:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        
class Perusahaan:
    def __init__(self, nama, pekerja):
        self.nama = nama
        self.pekerja = pekerja
        
    def daftar_pekerja1(self):
        for pekerja in self.pekerja:
            print("Longrich", pekerja.nama, pekerja.umur)
            
    def daftar_pekerja2(self):
        for pekerja in self.pekerja:
            print("Replay.net", pekerja.nama, pekerja.umur)

pekerja1 = Pekerja("Lais Cakrawati", 19)
pekerja2 = Pekerja("Dewi Kurnia", 20)
perusahaan1 = Perusahaan("Longrich", [pekerja1])
perusahaan2 = Perusahaan("Replay.net", [pekerja2])
perusahaan1.daftar_pekerja1()
perusahaan2.daftar_pekerja2()