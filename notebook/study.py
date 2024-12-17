# GİRİLEN SAYININ TEK Mİ ÇİFT Mİ OLDUĞUNU BULAN KOD

"""

sayi =int(input("bir sayı girin: "))

if sayi%2 == 0 :
    print("sayı çift")

else:
    print("sayı tek")
    
"""

# GİRİLEN SAYININ RAKAMLARI ÇARPIMINI BULAN KOD

"""

sayi = input("bir sayı girin: ")
carpim = 1

for rakam in sayi :
    carpim = carpim * int(rakam)

print(carpim)

"""

# GİRİLEN SAYININ RAKAMLARI TOPLAMINI BULAN KOD


""""
sayi = input("bir sayı girin: ")
toplam = 0

for rakam in sayi :
    toplam += int(rakam)

print(toplam)

"""

# VERİ TİPİ DÖNÜŞÜMLERİ

"""

a = 55
print(float(a))  (55.0)

b = 4.5
print(int(b))  (4)

a = 12
b = 6
print(float(a/b))  (2.0)

"""

# GİRİLEN SAYININ MUTLAK DEĞERİNİ BULMA 

"""

sayi = float(input("Bir sayı girin: "))

if sayi < 0 :
    sayi = sayi*-1

print(sayi)

"""

# EKRANA 10 DEFA "MERHABA DÜNYA" YAZDIRMA

"""
print("Merhaba Dünya\n" * 10)

"""

"""

for i in range(10):
    print("Merhaba Dünya")

"""

"""

sayac = 0 
while sayac < 10 :
    print("Merhaba Dünya")
    sayac = sayac + 1 
    
"""

# TUPLE

"""

demet = (1,2,1,3,5,1,"taha",7,8)
print(type(demet)) demet isimli tuple ın veri tipi öğrenildi
print(demet[0]) demet in sıfırıncı elemanı 
print(demet[2:]) demet in ikinciden başlayarak en sona kadar olan bütün elemanları
print(demet.index("taha")) "taha" isimli elemanın kaçıncı indekste olduğu belirlendi 
print(demet.count(1)) 1 in kaç defa demet içinde geçtiği belirlendi

"""

# DİCTİONARY

"""

sözlük1 = {"sıfır":0,"bir":1,"iki":2,"üç":3}
print(sözlük1["bir"])
print(sözlük1.values())

"""

"""

print(bool(12))
print(bool(0))

"""

"""

print("a" in "Merhaba")
print(4 in [1,2,3,4])

"""

"""

liste elemanlarını toplama : 

liste = [1,2,3,4,5,6,7]
toplam = 0

for i in liste : 
    toplam = toplam + i 
    
print(toplam)

"""

"""

çift elemanlarıbastırma

liste = [1,2,3,4,5,6,7,8,9]

for eleman in liste:
    if eleman % 2 == 0:
        print(eleman)

"""

"""

her bir karkateri 3 ile çarpma

s = "Python"

for karakter in s :
    print(karakter * 3 )
    
"""

"""

demetler içindeki elemanları çarpma

liste = [(1,2,3),(4,5,6),(7,8,9),(10,11,12)]

for (i,j,k) in liste :
    print(i*j*k)

"""


"""

faktoriyel hesabı

n = int(input("Faktöriyeli alınacak sayıyı girin: "))
faktoriyel = 1 

for i in range(1, n+1):
    faktoriyel = faktoriyel*i

print(faktoriyel)

"""
"""

n tane sayının toplamı

n = int(input("Kaç tane sayı toplanacak? "))
toplam = 0

for i in range(n):
    sayi = int(input("Toplanacak sayıyı girin: "))
    toplam = toplam + sayi

print(toplam)

"""

"""

asal sayı

n = int (input("bir sayı girin : "))
say = 0 

for i in range(2,n):
    if n%i == 0 :
        say= say + 1 
        break

if say == 0 : 
    print("sayı asal") 
else: 
    print("sayı asal değil ")

"""

"""

urunler = [
    {"name" : "samsung S6" , "price" : "3000"},
    {"name" : "samsung S7" , "price" : "4000"},
    {"name" : "samsung S8" , "price" : "5000"},
    {"name" : "samsung S9" , "price" : "6000"},
    {"name" : "samsung S10" , "price" : "7000"}
]

toplam = 0 

for urun in urunler : 
    fiyat = int(urun["price"])
    toplam = toplam + fiyat 

print(toplam)

"""

"""

urunler = [
    {"name" : "samsung S6" , "price" : "3000"},
    {"name" : "samsung S7" , "price" : "4000"},
    {"name" : "samsung S8" , "price" : "5000"},
    {"name" : "samsung S9" , "price" : "6000"},
    {"name" : "samsung S10" , "price" : "7000"}
]

for urun in urunler: 
    if int(urun["price"]) <= 5000 : 
        print(urun["name"])

"""

"""
isim adlı değişkenin içindeki stringin elemanlarını tersten yazdırma

isim = "tkcode"

for i in reversed(isim) : 
    print(i)
    
"""

"""
sehirler listesinin elemanlarını karakter sayılarıyla birlikte ekrana yazdırma

sehirler = ["Edirne", "Konya", "Ankara", "İstanbul", "Tekirdağ"]

for sehir in sehirler : 
    print(sehir, len(sehir))

"""

"""
sehirler adlı listedeki elemanlardan 6 karakterli olanları ekrana yazdırma

sehirler = ["Edirne", "Konya", "Ankara", "İstanbul", "Tekirdağ"]

for sehir in sehirler : 
    if len(sehir) == 6 : 
        print(sehir)

"""

"""
sayilar isimli listedeki çift sayılı elemanların toplamını hesaplama ve ekrana yazdırma 

sayilar = [12, 43, 11, 56, 43, 12, 8, 6, 43, 21, 23]

cift_toplam = 0 

for sayi in sayilar :
    if sayi % 2 == 0 : 
        cift_toplam+= sayi

print(cift_toplam)

"""

"""sozluk = {"a": 10 , "b": 20 , "c": 30 , "d": 40}

for i,j in sozluk.items(): 
    print(i,j)"""

"""notlar = {"Matematik" : 70, "Türkçe":80, "Programlama Temelleri": 50}
toplam = 0 

for notu in notlar.values():
    toplam = toplam + notu

ortalama = toplam / len(notlar.values())

print(ortalama)"""
"""
name = input("Your name: ")
surname = input("Your surname: ")
print("Hello", name , surname)

vize = int(input("Your vize note: "))
final = int(input("Your final note: "))
average = (vize + final) / 2 
print("Your vize note: {}\nYour final note: {}\nYour average: {}".format(vize,final,average))
"""

"""
replace ile istediğimiz harfi istediğimiz başka bir harfle değiştirdik

txt = "Hello World"
txt = txt.replace("H", "J")
print(txt)
"""
"""
mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist)
    
"""

"""a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print(max(a,b,c))"""


"""print("Üçgenin kenar uzunluklarını girin: ")

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if abs((a+b) > c) and abs((a+c) >b) and abs((b+c) > a):

    if a == b and a == c : 
         print("Eşkenar üçgen")

    elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
         print("İkizkenar üçgen")

    else : 
         print("Çeşitkenar üçgen")

else: 
    print("Üçgen belirtmiyor.")"""

"""for i in range(1,1000):
    if i % 9 == 0 :
        print(i)"""


"""

1-100 arasındaki sayıları 100 den başlayarak geriye doğru yazdırma

i = 100 

while i > 0 : 
    print(i)
    i = i - 1
    
"""

"""bas = int(input("Başlangıç: "))
bit = int(input("Bitiş: "))

i = bas 

while i < bit + 1 : 
    if i%2 == 1 : 
        print(i)
    i = i +1
"""

"""
for sayi in range(1,5):
    print("*" * sayi)
"""

"""sifre = ""

while sifre != "123456" : 
    sifre = input("Şifre: ")

print("Şifre doğru.")
"""

"""sayi = int(input("1-100 arası bir sayı girin: "))
i = 0 

while i < 101 : 
    i = i + 1
    if i == sayi :
        continue
    print(i)
    
"""

"""
liste = ["fenerbahçe", "galatasaray", "beşiktaş"]
liste1 = [takim[0] for takim in liste] #liste adlı listedeki elemanlar istenilen şekilde liste1 adlı listeye eklendi.

print(liste1)"""

"""while True:
    s = input("Bir sayı girin: ")
    if s == "iptal": 
        break 
    if len(s) <= 3: 
        continue 
    
    print("En fazla üç haneli bir sayı girebilirsiniz.")"""


# MÜKEMMEL SAYI 

"""sayi = int(input("Bir sayı girin: "))
toplam = 0 
i = 1 

while i < sayi : 
    if sayi % i == 0 : 
        toplam += i 

    i += 1

if toplam == sayi : 
    print("Sayı mükemmel.")

else: 
    print("Sayı mükemmel değil. ")"""

# ARMSTRONG SAYISI

"""sayi = input("Bir sayı girin: ")
toplam = 0 

for i in sayi: 
    toplam += int(i) ** len(sayi)

print(sayi)
print(toplam)

if toplam == int(sayi) : 
    print("Sayı armstrong sayısıdır. ")

else: 
    print("Sayı armstrong sayısı değildir. ")"""

# ÇARPIM TABLOSU 1-10

"""for i in range(1,11) : 
    print("*************")
    for j in range(1,11) : 
        print("{} x {}= {}".format(i,j,i*j))"""

"""list = [ i for i in range(1,101) if i % 2 == 0 ]
print(list)"""

