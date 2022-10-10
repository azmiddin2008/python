class Gishlar():
    sifati = True

class Hom_gish(Gishlar):
    
    def sifat(self):
        print("Bu gish 50 foiz yaxshi")

class Pishi_gish(Hom_gish):
    
    def chidamliligi(self):
        print("Chidamliligi 100 foiz")
        
class Blo_gish(Pishi_gish):
    
    def ogirligi(self):
        print("Ogirligi 20kg")
        
gish = Hom_gish()
gish2 = Pishi_gish()
gish3 = Blo_gish()

print(gish.sifati)
gish2.sifat()
gish3.chidamliligi()


 