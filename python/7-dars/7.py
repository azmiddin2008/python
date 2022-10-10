# 2d lists  malumotlar saqledi

# yigitlar = ["Olim","Iskandar", "Shavkat", "Momin"]
# qizlar = ["Ruhsora", "Rano", "Muhlisa", "Muslima"]
# kattalar = ["Olmaxon", "Fotima", "Mukarram", "Omatoy"]

# ismlar = [yigitlar, qizlar, kattalar]

# for y in ismlar:
#     for x in y:
#         print(x, end=",  ")

# 2-mavzu:Tuple - listga oxshash, lekin malumot qosha olmaymiz va umumuman ozgartira olmaymiz

# ismlar2 = ["Olim","Iskandar", "Shavkat", "Momin", "Olim",]
# print(ismlar2.count("Olim")) --> sozni necha marta qatnashganini aniqlab beradi
# print(ismlar2.index("Olim")) --> sozni yoki gapni nechinchi qatordaligini aniqlab beradi
# if "Olim" in ismlar2:
#     print("Olim shu yetda! ") -->bor yoki yog'ligini aniqlab beradi

# set moduli --> Bunda bir xil  malumotlarni bor bolishiga yol qoymaydi]

# ismlar3 = {"Olim","Iskandar", "Shavkat", "Momin"}
# ismlar3.add("Azizbek")
# ismlar3.remove("Olim")



# for x in sorted(ismlar3):
#     print(x, end=": ")

# dictionary - key, value dan iborat listlar boladi

poytaxtlar = {
    "UZB": "Tashkent",
    "CHNA": "Pekin",
    "USA": "Washintong",
    "FR": "Paris"
}
print(poytaxtlar["FR"])