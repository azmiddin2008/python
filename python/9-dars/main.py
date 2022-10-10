import random
# *args --> ko'p malumotlar bilan ishlash(parametrlar va argumentlar)
# def son(*args):
#     raqam = 0
#     for x in args:
#         raqam += x
#     return raqam
    
# print(son(10, 10, 20, 30, 40, 50,60))

# randomlar, randint

sanoq = random.randint(1, 100)
print(sanoq)

# choice metodi
# ismlar = ["Azmiddin", "Faxriddin", "Hotambek","Ruxsora", "Muhlisa", "Salom"]
# y = random.choice(ismlar)
# if y == "Ruxsora":
#     print(y + " chiqdi va tanlandi!")
# else:
#     print(y + " chiqdi va tanlanmadi!")

# Shuffle metodi --> listlarni ichidagi malumotlarni random qilib beradi
# ismlar = ["Azmiddin", "Faxriddin", "Hotambek","Ruxsora", "Muhlisa", "Salom"]
# random.shuffle(ismlar)
# for x in ismlar:
#     print(x, end=', ')

# fayllar bilan ishlash
# fayl = open("C:\\Users\\IT Center\\Documents\\salom.txt", "r")
# print(fayl.read())

# fayl = open("frontend/text.txt", "w")
# fayl.write("""
# I am victor
# I am Best player
           
#            """)

