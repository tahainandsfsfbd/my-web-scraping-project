
# BİR ÖĞRENCİNİN İKİ NOTUNUN ORTALAMASINI HESAPLAYAN VE ÇIKAN SONUCA GÖRE EKRANA İYİ VEYA KÖTÜ YAZDIRAN ALGORİTMA# 

not1 = float(input("İlk notu gir: "))
not2 = float(input("İkinci notu gir: "))
ort = (not1 + not2) / 2

if ort >= 70 :
    print("İYİ")

else:
    print("KÖTÜ")
