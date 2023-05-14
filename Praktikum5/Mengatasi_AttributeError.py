print('Lais Cakrawati\n210511002\nT121A(R1)\n')

class Anjing:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

anjing = Anjing("yeontan", "teacup pomeranian")

try:
    print(anjing.pemilik)
except AttributeError:
    print("Objek tidak memiliki atribut yang diminta!")