
# PROGRAMLAMA ÖDEVİ 

"""

KULLANICIDAN ALINAN BOY VE KİLO DEĞERLERİYLE BEDEN KİTLE ENDEKSİ HESAPLA 

Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

BKİ 18.5'un altındaysa -------> Zayıf

BKİ 18.5 ile 25 arasındaysa ------> Normal

BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

BKİ 30'un üstündeyse -------------> Obez



print("Beden Kitle Endeksi")

kilo = float(input("Kilonuzu girin: "))
boy = float(input("Boyunuzu(m) girin: "))

bki = kilo / boy**2

if bki < 18.5 :
    print("BEDEN KİTLE ENDEKSİNİZ = {}".format(bki))
    print("Zayıf")

elif bki >= 18.5 and bki < 25  :
    print("BEDEN KİTLE ENDEKSİNİZ = {}".format(bki))
    print("Normal")

elif bki >= 25 and bki < 30 :
    print("BEDEN KİTLE ENDEKSİNİZ = {}".format(bki))
    print("Fazla Kilolu")

else :
    print("BEDEN KİTLE ENDEKSİNİZ = {}".format(bki))
    print("Obez")

"""



"""

KULLANICIDAN 3 TANE SAYI AL VE EN BÜYÜĞÜNÜ EKRANA YAZDIR

sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))
sayi3 = int(input("Üçüncü sayıyı girin: "))

if sayi1 >= sayi2 and sayi1 >= sayi3 :
    print(sayi1)

elif sayi2 >= sayi1 and sayi2 >= sayi3 :
    print(sayi2)

elif sayi3 >= sayi2 and sayi3 >= sayi1 :
    print(sayi3)

"""

"""

Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF
    


vize1 = float(input("İlk vize sonucu: "))
vize2 = float(input("İkinci vize sonucu: "))
final = float(input("Final sonucu: "))
toplam = (vize1*30)/100 + (vize2*30)/100 + (final*40)/100

print(toplam)

if toplam >= 90:
    print("AA")

elif toplam >= 85:
    print("BA")

elif toplam >= 80:
    print("BB")

elif toplam >= 75:
    print("CB")

elif toplam >= 70:
    print("CC")

elif toplam >= 65:
    print("DC")

elif toplam >= 60:
    print("DD")

elif toplam >= 55:
    print("FD")

elif toplam < 55:
    print("FF")

"""

"""

İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir 
dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , 
eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. 

Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.



sekil = input("Hangi geometrik şeklin tipini öğrenmek istiyorsunuz ?(Üçgen / Dörtgen)  ")

if sekil == "Dörtgen" : 
    print("Kenar uzunluklarını girin")
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    d = int(input("d: "))

    if a==b and a==c and a==d :
        print("Kare")
    
    elif a==b and c==d :
        print("Dikdörtgen")
    
    else: 
        print("Dörtgen")

elif sekil == "Üçgen" : 
    print("Kenar uzunluklarını girin")
    e = int(input("e: "))
    f = int(input("f: "))
    g = int(input("g: "))
    
    if abs(e+f) > g and abs(e+g) > f and abs(g+f) > e :  #üçgen olma kuralı 
        if e == f and e == g :
            print("Eşkenar Üçgen") 
        
        elif (e == f and e != g) or (e == g and e != f) or (f == g and f != e) :
            print("İkizkenar Üçgen")

        else:
            print("Çeşitkenar Üçgen")
    else:
        print("Üçgen belirtmiyor")

else: 
    print("Şekil geçersiz...")

"""

