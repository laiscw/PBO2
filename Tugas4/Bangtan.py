print('Lais Cakrawati\n210511002\nT121A(R1)\n')

class Nama_Member:
    def __init__(self,nama=None):
        if nama is None:
            self.nama = []
        else:
            self.nama = nama

    def add_nama(self,nama):
        self.nama.append(nama)

    def daftar_nama(self):
        for nama in self.nama:
            print(f'Nama\t\t: ',nama.nama)
            print(f'Umur\t\t: ',nama.genre)
            print(f'Posisi\t\t: ',nama.tgl_rilis)

class Nama:
    def __init__(self,nama,genre,tgl_rilis):
        self.nama = nama
        self.genre = genre
        self.tgl_rilis = tgl_rilis

    def get_tgl_rilis(self):
        return self.tgl_rilis

    def get_genre(self):
        return self.genre
    
    def get_tgl_rilis(self):
        return self.tgl_rilis

class Member:
    def __init__(self,name_member,nama_member):
        self.name_member = name_member
        self.nama_member = nama_member

    def tampil(self):
        print(f'\nNama Grup\t: {self.name_member}\n')

nama1 = Nama('Kim Namjoon', 28, "Rapper")
nama2 = Nama('Kim Seok jin', 30, "Vocalist")
nama3 = Nama('Min Yoon-gi', 30, "Rapper")
nama4 = Nama('Jung Ho-seok', 29, "Dancer")
nama5 = Nama('Park Jimin', 27, "Vocalist/Dancer")
nama6 = Nama('Kim Taehyung', 27, "Visual")
nama7 = Nama('Jeon Jungkook', 25, "Golden Maknae")
nama_member = Nama_Member([nama1, nama2, nama3, nama4, nama5, nama6, nama7])
member = Member('BTS', nama_member)
member.nama_member.nama
member.tampil()
print("="*40)
member.nama_member.daftar_nama()