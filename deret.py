deretAngka = []
faktorTambah = 3
nilaiDeret = 1

n = int(input("Masukkan Nilai N: "))

for i in range(1, n+1):
    deretAngka.append(nilaiDeret)
    nilaiDeret += faktorTambah
    faktorTambah += 1
    print(deretAngka)

