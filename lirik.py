lirik = "It was easy as 1, 2, 1, 2, 3, 4 There is only one thing to do"
jumlahHuruf = 0
jumlahAngka = 0

for i in lirik:
    if i.lower() in "itwaseasyasthereisonlyonethingtodo":
        jumlahHuruf = jumlahHuruf + 1
    if i.lower() in "1234":
        jumlahAngka = jumlahAngka + 1

print ("Jumlah huruf ", jumlahHuruf)
print("Jumlah angka ", jumlahAngka)
print("Itwaseasyas1,2,1,2,3,4Thereisonlyonethingtodo")
