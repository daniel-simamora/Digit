'''
Soal:
Membuat function digitAwal(a,b) yang menghasilkan angka pertama dari operasi pangkat,
kemudian function digitAkhir() yang menghasilkan angka terakhir dari operasi pangkat.
'''

def digitAwal(a,b):
    # Function ini akan mengembalikan nilai sebagai berikut:
    # Hasil perpangkatan a**b yang diubah menjadi string
    # Kemudian string tersebut akan di-index [0] 
    # untuk mengambil digit pertamanya
    return str(a**b)[0]

def digitAkhir(a,b):
    # Function ini akan mengembalikan nilai sebagai berikut:
    # Hasil perpangkatan a**b yang diubah menjadi string
    # Kemudian string tersebut akan di-index [-1] 
    # untuk mengambil digit terakhirnya
    return str(a**b)[-1]

# TESTING:

# Digit Awal:
print('Digit awal:')
print(digitAwal(10,8))
print(digitAwal(2,3))
print(digitAwal(6,3))
print() # Space Kosong

# Digit Akhir:
print('Digit akhir:')  
print(digitAkhir(10,8))
print(digitAkhir(2,3))
print(digitAkhir(6,3))
