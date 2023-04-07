print('Lais Cakrawati\n210511002\nT121A(R1)\n')

class Penulis:
    def __init__(self,nama):
        self.nama = nama
        self.inventory = Inventory()
    
    def tampil(self):
        print(f'\nPenulis\t\t:  {self.nama}\n')

class Buku:
    def __init__(self,judul,publish,penerbit):
        self.judul = judul
        self.publish = publish
        self.penerbit = penerbit

    def get_judul(self):
        return self.judul

    def get_publish(self):
        return self.publish

    def get_penerbit(self):
        return self.penerbit

class Inventory:
    def __init__(self):
        self.books = []

    def add_buku(self,buku):
        self.books.append(buku)

    def daftar_buku(self):
        for buku in self.books:
            print(f'Judul\t\t: ',buku.judul)
            print(f'Terbit\t\t: ',buku.publish)
            print(f'Penerbit\t: ',buku.penerbit)

penulis1 = Penulis('Andrea Hirata')
edensor = Buku('Edensor', 'Jakarta, 2007', 'Mediakita')
ayah = Buku('Ayah', 'Jakarta, 2015', 'Mediakita')
guruaini = Buku('Guru Aini', 'Jakarta, 2019', 'Mediakita')
ingkar = Buku('Ingkar', 'Jakarta, 2020', 'Mediakita\n')
penulis1.inventory.add_buku(edensor)
penulis1.inventory.add_buku(ayah)
penulis1.inventory.add_buku(guruaini)
penulis1.inventory.add_buku(ingkar)
penulis1.inventory.books
penulis1.tampil()
penulis1.inventory.daftar_buku()