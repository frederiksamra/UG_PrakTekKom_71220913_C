print("Pemeriksaan Kelipatan 9")
dua = int(input(" Masukkan angka kelipatan 9 yang ingin di periksa: "))
def kelipatan_9():
    answer = (dua%9)
    return answer

if kelipatan_9()==0:
    print("BENAR")
else:
    print("SALAH")
