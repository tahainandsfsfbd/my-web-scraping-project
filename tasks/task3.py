
# MÜKEMMEL SAYI BULMA 

"""sayi = int(input("Bir sayı girin: "))
toplam = 0 

for i in range(1, sayi): 
    if sayi % i == 0 : 
        toplam += i

if toplam == sayi :
    print(sayi,toplam, "Sayı mükemmel sayıdır.")
    
else:
    print(sayi, toplam, "Sayı mükemmel sayı değildir.")"""



"""sayi = int(input("Bir sayı girin: "))
i = 1 
toplam = 0 

while i < sayi : 
    if sayi % i == 0 :
        toplam += i 

    i += 1 

if toplam == sayi :
    print(sayi, "mükemmel sayıdır.")

else:
    print(sayi, "mükemmel sayı değildir.")
"""

# ARMSTRONG SAYISI BULMA 

"""sayi = input("Bir sayı girin: ")
toplam = 0 

for i in sayi : 
    toplam = toplam + int(i) ** len(sayi)

if toplam == int(sayi) : 
    print(sayi, "Armstrong sayısıdır.")

else: 
    print("Sayı armstrong sayısı değildir.")"""



"""sayı = input("Sayı:")
basamak_sayisi = len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0

gecici_sayı = sayı

while (gecici_sayı > 0):
    
    basamak = gecici_sayı % 10
    
    toplam += basamak ** basamak_sayisi
    
    gecici_sayı //= 10
    

if (toplam == sayı):
    print(sayı,"bir armstrong sayısıdır.")
else:
    print(sayı,"bir armstrong sayısı değildir.")"""


# ÇARPIM TABLOSU (1-10)

"""for i in range(1,11) : 
    print("*************************")
    for j in range(1,11) : 
        print("{} x {} = {}".format(i,j,i*j))"""

    
# KULLANICININ GİRDİĞİ SAYILARI TOPLAMA

"""toplam = 0 

while True:

    toplam = 0 
    sayi = input("Bir sayı girin: ")

    if sayi == "q" : 
        print("Programdan çıkılıyor.")
        break
    
    toplam += int(sayi)

print(toplam)"""

# 1-101 ARASI SAYILARDAN 3 E TAM BÖLÜNENLERİ BASTIRMA

"""for i in range(1,101) : 
    if i % 3 != 0 : 
        continue
    print(i)"""

# 1-101 ARASI SAYILARDAN SADECE ÇİFT OLANLARI BİR LİSTEYE ATMA

"""list2 = [i for i in range(1,101) if i % 2 == 0 ]

print(list2)
    """

    




