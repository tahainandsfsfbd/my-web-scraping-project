
# KOŞULLU KULLANICI GİRİŞİ 

print("""
****************************
KULLANICI GİRİŞİ
******************************""")

sys_kullanici = "ttaha"
sys_parola = "12345"

kullanici_adi = input("Kullanıcı Adı: ")
parola = input("Parola: ")

if kullanici_adi == sys_kullanici and parola != sys_parola :
    print("Parola hatalı.")

elif kullanici_adi != sys_kullanici and parola == sys_parola :
    print("Kullanıcı adı hatalı.")

elif kullanici_adi != sys_kullanici and parola != sys_parola :
    print("Kullanıcı adı ve parola hatalı.")

else: 
    print("Sisteme başarıyla giriş yapıldı...")



"""

ALTERNATİF KISA VE DAHA DETAYSIZ ÖRNEĞİ 

if kullanici_adi != sys_kullanici or sys_parola != parola : 
    print("Kullanıcı adı veya parola hatalı...")

else:
    print("Sisteme başarıyla giriş yapıldı...")
    
"""