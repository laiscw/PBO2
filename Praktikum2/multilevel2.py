#Nama   : Lais Cakrawati
#Kelas  : R1
#NIM    : 210511002

class Perusahaan:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} speaks")

class Karyawan(Perusahaan):
    def __init__(self, name, nip):
        super().__init__(name)
        self.nip = nip
    def data(self):
        print(f"{self.name} dengan nip {self.nip}")

class Informasi(Karyawan):
    def __init__(self, name, nip, alamat, sejak):
        super().__init__(name, nip)
        self.alamat = alamat
        self.sejak = sejak
    def speak(self):
        print(f"{self.name} Beralamatkan {self.alamat}, bekerja sejak {self.sejak}")
        print("="*54)
        
Informasi = Informasi("Lais Cakrawati", 210511002, "Kuningan", 2020)
Informasi.data() 
Informasi.speak() 
