print('Lais Cakrawati\n210511002\nT121A(R1)\n')

list_angka = [2, 4, 6]

try:
    value = list_angka[8]
    
except IndexError:
    print("Index yang diminta melebihi jumlah elemen dalam list!")