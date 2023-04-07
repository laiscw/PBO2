print('Lais Cakrawati\n210511002\nT121A(R1)\n')

class Kpop:
    def __init__(self,grup,year,fandom):
        self.grup = grup
        self.year = year
        self.fandom = fandom

class Agensi:
    def __init__(self,nama,kpop):
        self.nama = nama
        self.kpop = kpop

    def daftar_kpop(self):
        print(f'\nAgensi\t: {self.nama}\n')
        for kpop in self.kpop:
            print(f'Nama Grup\t: ',kpop.grup)
            print(f'Debut\t\t: {kpop.year}')
            print(f'Nama Fandom\t: {kpop.fandom}')

kpop1 = Kpop('BTS', 2013, "Army")
kpop2 = Kpop('Tomorrow X Together', 2019, "MOA")
agensi1 = Agensi('BigHit Entertaiment', [kpop1, kpop2])
kpop3 = Kpop('Seventeen', 2015, "Carat")
kpop4 = Kpop('NUEST', 2012, "L.O.A.E")
agensi2 = Agensi('Pledis Entertaiment', [kpop3, kpop4])
agensi1.daftar_kpop()
print('='*40)
agensi2.daftar_kpop()