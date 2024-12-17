
# DÖNGÜLERLE GELİŞMİŞ BİR KULLANICI GİRİŞİ 

"""
ÖNCE DOĞRU OLAN KULLANICI ADI VE PAROLA BELİRLENDİ.
DAHA SONRA GİRİŞ HAKKI VERİLDİ.
DAHA SONRA WHİLE TRUE İLE SONSUZ BİR DÖNGÜ BAŞLATILDI.
DAHA SONRA KULLANICIDAN KULLANICI ADI VE ŞİFRE İSTENDİ.
KOŞULLAR BELİRLENDİ.
ŞİFRE VEYA KULLANICI ADI VEYA HER İKİSİ DE YANLIŞ OLDUĞU TAKDİRDE GİRİŞ HAKKI AZALTILIR VE GİRİŞ HAKKI SIFIRA İNERSE DÖNGÜDEN ÇIKAR.
EĞER ŞİFRE DOĞRUYSA DÖNGÜ SONLANIR.

"""

sys_kullanici_adi = "ttaha"   #sistemde kayıtlı olduğunu düşündüğümüz kullanıcı adı 
sys_parola = "12345"    #sistemde kayıtlı olduğunu düşündüğümüz parola 

giris_hakki = 3 

while True :   #kullanıcı doğru giriş yaptığında veya giriş hakkı bittiğinde sonlanacak 
    kullanici_adi = input("Kullanıcı adı: ")
    parola = input("Parola: ")

    if (kullanici_adi != sys_kullanici_adi and parola == sys_parola) :                     
        print("Kullanıcı adı hatalı.")                                                          
        giris_hakki -= 1                                                                       
        print("Giriş hakkı: ", giris_hakki)                                                     
                                                                                            
    elif (kullanici_adi == sys_kullanici_adi and parola != sys_parola) :                   
        print("Parola hatalı.")                                                                 
        giris_hakki -= 1                                                                    
        print("Giriş hakkı: ", giris_hakki)                                                
                                                                                                
    elif (kullanici_adi != sys_kullanici_adi and parola != sys_parola) :                    
        print("Kullanıcı adı ve parola hatalı.")                                               
        giris_hakki -= 1                                                                   
        print("Giriş hakkı: ", giris_hakki)                                                             
                                                                                            
    else:                                                                                  
        print("Sisteme başarıyla giriş yapıldı.")                                          
        break

    if giris_hakki == 0 :
        print("Giriş hakkınız bitti.")
        break
    




