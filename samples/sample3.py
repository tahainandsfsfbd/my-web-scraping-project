
# BASİT HESAP MAKİNESİ 

print("""***************************************
HESAP MAKİNESİ PROGRAMI

İŞLEMLER : 

1. TOPLAMA
2. ÇIKARMA
3. ÇARPMA
4. BÖLME

**************************************
""")

a = int(input("Birinci sayı: "))
b = int(input("İkinci sayı: "))
islem = input("İşlemi giriniz(1,2,3,4): ")

if islem == "1" : 
    print("{} ile {} toplamı {} dir.".format(a,b,a+b))

elif islem == "2" : 
    print("{} ile {} farkı {} dir.".format(a,b,a-b))

elif islem == "3" : 
    print("{} ile {} çarpımı {} dir.".format(a,b,a*b))

elif islem == "4" : 
    print("{} ile {} bölümü {} dir.".format(a,b,a/b))

else:
    print("Geçersiz işlem...")
    