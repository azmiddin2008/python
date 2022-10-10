# class komputer:
#     def __init__(self, nomi, hotirasi, joyi, diskavat, narxi, brendi, yaratuvchisi, songi_modeli, tezligi, kp,):
#         self.nomi = nomi
#         self.hotirasi = hotirasi
#         self.joyi = joyi
#         self.diskavat = diskavat
#         self.narxi = narxi
#         self.brendi = brendi
#         self.yaratuvchisi = yaratuvchisi
#         self.songimodeli = songi_modeli
#         self.tezligi = tezligi
#         self.kp = kp
#     def __str__(self):
#         return f"Kompyuter nomi {self.nomi}. Hotirasi {self.hotirasi}. Ishlab chiqarilgan joyi {self.joyi}. Diskavati {self.diskavat}. Narxi {self.narxi}. Kompyuter brendi {self.brendi}. Yaratuvchisi {self.yaratuvchisi}. Songi modeli {self.songimodeli}. Tezligi {self.tezligi}. Kelabayti {self.kp}"

# Monti level inheritance --> clasdan clasga avlod olish

class Hayvon():
    
    trik = True
    
class It(Hayvon):
    
    def yemoq(self):
        print("Bu it ovqat yiyapdi")
        
class Qush(It):
    
    def uchmoq(self):
        print("Bu qush uchuyapdi")

it = It()    
qush = Qush()

print(it.trik)
qush.yemoq()
it.yemoq()