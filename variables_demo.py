"""
Uygulama 1: Bir Ogrencinin aşağidaki bilgileri için gerekli değiişkenleri oluşturunuz.
Öğrenci adı
Öğrenci soyadı:
Öğrenci ad + soyad
Öğrenci numarası
Öğrenci cinsiyet
Öğrenci tc kimlik
Öğrenci doğum yılı
Öğrenci adres bilgisi
Öğrenci yaşı

"""


ogrenciAdi="Emirhan"
ogrenciSoyAdi="Aydemir"
ogrenciAdiSoyAdi = f'{ogrenciAdi} {ogrenciSoyAdi}'
ogrenciNumarasi=60 

ogrenciCinsiyet=True  #Erkek
print(ogrenciCinsiyet)

ogrenciCinsiyet=False  #Kadin
print(ogrenciCinsiyet)

ogrenciTcKimlik=12345678923
ogrenciDogumYili=2003
ogrenciAdresBilgisi="Firat Universisiti"
ogrenciYasi=2025 - ogrenciDogumYili

print(ogrenciAdi)
print(ogrenciSoyAdi)
print(ogrenciAdiSoyAdi)

print(ogrenciYasi)


"""
Uygulama 2: Aşağıdaki ürünlerin toplam bilgisini hesasplayınız.

    Ürün 1 => 50     TL
    Ürün 2 => 60.5   TL
    Ürün 3 => 356.45 TL

"""

urun1=50
urun2=60.5
urun3=365.45

toplam=urun1+urun2+urun3
print("Urunlerin Toplami : ",toplam)