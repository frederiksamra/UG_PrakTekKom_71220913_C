def penjumlahan(bilangan_pertama, bilangan_kedua):
    tambah = (bilangan_pertama + bilangan_kedua)
    return tambah
def pengurangan(bilangan_pertama, bilangan_kedua):
    kurang = (bliangan_pertama - bilangan_kedua)
    return kurang
def perkalian(bilangan_pertama, bilangan_kedua):
    kali = (bilangan_pertama * bilangan_kedua)
    return kali
def pembagian(bilangan_pertama, bilangan_kedua):
    bagi = (bilangan_pertama/bilangan_kedua)
    return bagi
print("==========================")
print("Operasi Matematika")
print("1. Jumlah      [+]")
print("2. Kurang      [-]")
print("3. Kali        [*]")
print("4. Bagi        [/]")
print("==========================")
operasi = input("Pilih Operasi :1/2/3/4) :" )
print("==========================")
bilangan_pertama = int(input("Masukkan bilangan pertama : "))
bilangan_kedua = int(input("Masukkan bilangan kedua : "))

if operasi == '1':
    print(f"Hasil operasi dari", bilangan_pertama, "+", bilangan_kedua, "=", penjumlahan(bilangan_pertama, bilangan_kedua))
elif operasi == '2':
    print(f"Hasil operasi dari", bilangan_pertama, "-", bilangan_kedua, "=", penjumlahan(bilangan_pertama, bilangan_kedua))
elif operasi == '3':
     print(f"Hasil operasi dari", bilangan_pertama, "*", bilangan_kedua, "=", penjumlahan(bilangan_pertama, bilangan_kedua))
elif operasi == '4':
     print(f"Hasil operasi dari", bilangan_pertama, "/", bilangan_kedua, "=", penjumlahan(bilangan_pertama, bilangan_kedua))

print("==========================")
print("Operasi Matematika")
print("1. Jumlah      [+]")
print("2. Kurang      [-]")
print("3. Kali        [*]")
print("4. Bagi        [/]")
print("==========================")
operasi = input("Pilih Operasi :1/2/3/4) :" )
print("==========================")
bilangan_pertama = int(input("Masukkan bilangan pertama : "))
bilangan_kedua = int(input("Masukkan bilangan kedua : "))

if operasi == '1':
    print(f"Hasil operasi dari", bilangan_pertama, "+", bilangan_kedua, "=", penjumlahan(bilangan_pertama, bilangan_kedua))
elif operasi == '2':
    print(f"Hasil operasi dari", bilangan_pertama, "-", bilangan_kedua, "=", penjumlahan(bilangan_pertama, bilangan_kedua))
elif operasi == '3':
     print(f"Hasil operasi dari", bilangan_pertama, "*", bilangan_kedua, "=", penjumlahan(bilangan_pertama, bilangan_kedua))
elif operasi == '4':
     print(f"Hasil operasi dari", bilangan_pertama, "/", bilangan_kedua, "=", penjumlahan(bilangan_pertama, bilangan_kedua))

