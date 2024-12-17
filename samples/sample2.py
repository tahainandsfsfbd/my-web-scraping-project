
# n TANE SAYININ ORTALAMASINI HESAPLAYAN KOD

num = int(input("Kaç tane sayının hesaplanacağını girin: "))
total_sum = 0

for n in range(num):
    numbers = float(input("İstediğiniz sayıyı girin: "))
    total_sum += numbers

avg = total_sum / num 

print(avg)


"""n = int(input("Kaç sayının ortalaması hesaplanacak: "))

toplam = 0 

for i in range(n):
    sayi = int(input("Bir sayı girin: "))
    toplam = toplam + sayi 

ortalama = toplam / n 

print(ortalama)"""