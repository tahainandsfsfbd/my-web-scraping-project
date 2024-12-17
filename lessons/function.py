
#FAKTORİYEL HESABI YAPAN FONKSİYON 

"""def faktoriyel(sayi): 
    faktoriyel = 1 

    if sayi == 0 or sayi == 1 : 

        print("Faktoriyel: ", faktoriyel)

    else:

        while sayi >= 1 : 
            faktoriyel *= sayi 
            sayi = sayi -1 

        print("Faktoriyel: ", faktoriyel)

faktoriyel(5)"""






#RETURN 

"""def toplama(a,b,c) : 
    return a+b+c

def ikiylecarp(a) : 
    return a*2

toplam = toplama(3,4,5)

print(ikiylecarp(toplam))
"""






"""def uclecarp(a): 
    print("1. fonksiyon çalıştı.")
    return a*3

def ikiyletopla(a): 
    print("2. fonksiyon çalıştı.")
    return a+2

def dordebol(a): 
    print("3. fonksiyon çalıştı.")
    return a / 4

print(dordebol(ikiyletopla(uclecarp(5))))"""






"""def toplama(a,b,c):
    return a + b + c
    print("Toplama fonksiyonu") # Çalıştırılmadı.

print(toplama(1,2,3))"""








"""def fonksiyon():
    a = 10 #yerel değişken
    print(a)

fonksiyon()
print(a) #değişken yok oldu o yüzden hata alındı.(name "a" is not defined)"""








"""c = 10 # Globalde tanımlanmış bir değişken 
def fonksiyon():
    c = 2 # Yerelde tanımlanmış bir değişken
    print(c)  # Yerel değişken kullanılıyor.

fonksiyon()
print(c)
"""








"""d = 10

def fonksiyon():
    global d
    
    d = 4
    print(d)
fonksiyon()
print(d)
"""






#LAMBDA

"""ikiylecarp = lambda x : x*2
print(ikiylecarp(3))"""










#FACTORİAL 

"""def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))

print(factorial(6))
"""






"""toplama = lambda a,b,c : a + b + c 
print(toplama(3,4,5))"""







#string ters çevirme

"""def terscevir(s) : 
    return s[::-1]

print(terscevir("python programlama"))"""


"""terscevir = lambda s:  s[::-1]    #lambda ile..
print(terscevir("Python Programlama"))
"""

















