class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def info(self):
        print(f"Nama: {self.nama}\nNPM: {self.nim}")

mahasiswaB = Mahasiswa("Lais Cakrawati", "210511002")
mahasiswaB.info()