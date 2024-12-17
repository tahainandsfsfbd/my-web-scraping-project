import random
import time 

sayi = random.randint(1,1000)
tahmin_sayisi = 10

while True:
    tahmin = input("Tahmin: ")
    
    if tahmin == "q" : 
        print("Görüşmek üzere...")
        break
    else:
        tahmin = int(tahmin)
        if tahmin < sayi :
            if tahmin_sayisi == 1:
                print("Tahmin hakkınız bitti!Doğru sayı: ",sayi)
                break
            else:
                print("Bilgiler sorgulanıyor")
                time.sleep(1)
                print("Daha büyük bir sayı deneyin.")
                tahmin_sayisi -= 1 
            
        elif tahmin > sayi : 
            if tahmin_sayisi == 1:
                print("Tahmin hakkınız bitti! Doğru sayı: ",sayi)
                break
            else:
                print("Bilgiler sorgulanıyor")
                time.sleep(1)
                print("Daha küçük bir sayı deneyin.")
                tahmin_sayisi -= 1

        else:
            print("Bilgiler sorgulanıyor")
            time.sleep(1)
            print("Tebrikler! Tahmininiz doğru..")
            break
    
    