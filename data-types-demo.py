# sourcery skip: use-fstring-for-concatenation
"""
    Daire Alani  : πr²
    Daire Çevresi : 2πr    
    ** Yari çapi verilen bir dairenin alan ve çevresini hesaplayiniz. (π: 3.14)
"""



pi=3.14

r=float(input("Yari Cap :"))

alan=pi*(r**r)

cevre=2*pi*r

sonuc="Alan : " + str(alan) + " cevre : " + str(cevre)
print(sonuc)


'''
    Bir aracin km cinsinden gittiği yol bilgisini mil olarak yazdiriniz.
    mil = km / 1.609344
'''
mesafeKm=float(input("Kac Km Yol Gitiiniz : "))
#mesafeKm=input()
mesafeMil = mesafeKm / 1.609344
mesafeMil=round(mesafeMil,2)

print(f"{mesafeKm} km = {str(mesafeMil)} mil. ")