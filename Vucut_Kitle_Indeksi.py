# Vücut Kitle İndeksi (VKİ) = Vücut Ağırlığı (kg.) / Boy uzunluğunun karesi (cm.)
# İdeal Kilo = Ulaşılmak istenen VKİ değeri * Boy uzunluğunun karesi
# Örnek İdeal Kilo = 24 * (1,60 * 1,60)= 61,4 kg
# Ben vücut yüzey alanını bu formülle hesaplıyorum: BSA = (ağırlığın0.425 x boy0.725) x 0.007184
# Gokhan Yavas -- gokhanyavas.com

programadi = "Vücut Kitle Indeksi Hesaplama"
print(programadi, "\n", "-"*len(programadi), sep="")

# vucut agirligini istiyoruz
va = input("Vücut Ağırlığı Giriniz :\n")
vucutagirligi = int(va)

#boy uzunlugunu istiyoruz
bu = input("Boy Uzunluğunuzu Giriniz :\n")
boyuzunlugu = int(bu)

print("-"*30)

#Vücut Yüzey Alanı hesapla
vya = pow(vucutagirligi, 0.425) * pow(boyuzunlugu, 0.725) * 0.007184
# vki hesaplamasi yapiyoruz
vki = (vucutagirligi / pow(boyuzunlugu, 2)) * 10000

#Vücut Yüzey Alanını yazdir
print("Vücut Yüzey Alanınız (BSA):\t", vya, "metrekare")

#Vücut Kitle Endeksini yazdir
print("Vücut Kitle indeksiniz (BMI):\t", vki, "kg / metrekare")

#Sonuç:
if vki >= 40:
    print("Sonuç:\t Aşırı Şişman (Morbid obez)")
elif vki >= 30:
    print("Sonuç:\t Şişman (Obez)")
elif 25 <= vki <= 30:
    print("Sonuç:\t Hafif şişman")
elif 20 <= vki <= 25:
    print("Sonuç:\t Normal kilolu")
elif 0 <= vki <= 19:
    print("Sonuç:\t Çok zayıf")

print("-"*30)