# name= input("İsim=")
# surname=input("Soyisim=")
# country=input("Yaşadığın yer=")

# print(f"İsmim {name} sayismim {surname} yaşadığım yer {country}.")












# itemprice = float(input("Ürün Tutarı="))
# discountpercentage = input("İndirim Yüzdesi= ")
# clear= discountpercentage.replace("%", "")
# clear = float(clear)

# print(f"Ürün fiyatı {itemprice} indirim yüzdesi {discountpercentage} yeni ürün fiyatı " + str(itemprice-itemprice*clear/100) + " kar miktarı " + str(itemprice*clear/100))











# birthyear= int(input("Doğum yılınız="))
# age= 2026-birthyear
# if age >= 18:
#     print(f"Yaşınız {age} ehliyet alabilirsiniz.")
# elif age<18:
#     print(f"Yaşınız {age } Ehliyet almanız için 18 yaşını doldurmanız lazım.")












vize = float(input("Vize notu= "))
final= float(input("Final notu= "))
periodgrade= vize*40/100 + final*60/100
print(f"Dönem notunuz {periodgrade}", end=" ")
if periodgrade==100:
    print("Harf notunuz AA")
elif 100>periodgrade>=90:
    print("Harf notunuz AB")
elif 90>periodgrade>=50:
    print("Harf notunuz BA")
elif 50>periodgrade>=35:
    print("Harf notunuz BB")
elif 35>periodgrade>=0:
    print("Dönemi geçemediniz.")
































