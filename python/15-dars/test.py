class Hayvon:
    trik = True

class Timsoh(Hayvon):
    
    def swim(self):
        print("Timsoh suza oladi")
        print("Yeya oladi")
        
class It(Timsoh):
    
    def eat(self):
        print("Yeya oladi va uchadi")
class Qush(It):
    def fly(self):
        print("Ucha oladi")
        
class Burgut(Qush):
    
    def tutmoq(self):
        print("Oljani tutadi")

class Bori(Burgut):
    
    def quvmoq(self):
        print("Oljani quvlaydi")
        
timsoh = Timsoh()
it = It()
qush = Qush()
burgut = Burgut()
bori = Bori()

print(timsoh.trik)

        