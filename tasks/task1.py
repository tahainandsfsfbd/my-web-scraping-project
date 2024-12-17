
# PROGRAMLAMA ÖDEVİ

"""

PROGRAMCIDAN ALINAN 3 SAYIYI ÇARPIP EKRANA YAZDIRMA ( FORMAT METODUYLA )

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

carpim = a * b * c

print("{} x {} x {} = {}".format(a, b, c, carpim))

"""

"""

KULLANICIDAN BOY VE KİLO DEĞERLERİNİ ALIP BEDEN KİTLE ENDEKSİNİ BULUN
( BEDEN KİTLE ENDEKSİ = KİLO / BOY(M)*BOY(M))


kilo = float(input("Kilonuz: "))
boy = float(input("Boyunuz(m): "))

bke = kilo / boy**2

print("Beden Kitle Endeksiniz: {}".format(bke))

"""

"""
KULLANICIDAN AD SOYAD VE NUMARA BİLGİSİ AL VE BU BİLGİLERİ ALT ALTA EKRANA YAZDIR

ad = input("Adınız: ")
soyad = input("Soyadınız: ")
numara = input("Telefon Numaranız: ")

print("\n{}\n{}\n{}\n".format(ad,soyad,numara))

"""

"""

KULLANICIDAN İKİ TANE SAYI İSTE VE BU SAYILARIN DEĞERLERİNİ BİRBİRLERİYLE DEĞİŞTİR

sayi1 = float(input("Bir sayı girin: "))
sayi2 = float(input("Bir sayı daha girin: "))

sayi1, sayi2 = sayi2, sayi1
print(sayi1, sayi2)

"""

"""

KULLANICIDAN BİR ÜÇGENİN DİK OLAN İKİ KENARINI ALIN VE HİPOTENÜSÜ HESAPLAYIN

dik_kenar1 = float(input("İlk dik kenar uzunluğu: ")) 
dik_kenar2 = float(input("İkinci dik kenar uzunluğu: "))
hipotenus = (dik_kenar1**2 + dik_kenar2**2)**0.5

print("Hipotenüs uzunluğu: {}".format(hipotenus))

"""