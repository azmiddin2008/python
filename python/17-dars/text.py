class Maktablar:
    
    def lider(self):
        print("Bu maktab juda ham yaxshi")

class Yomon:
    
    def yaxshimas(self):
        print("Birargi maktablar yaxshimas")
        
class Ortacha:

    def yomonmas(self):
        print("Bu maktab yomonmas")
        
class Eng_yaxshi:
    
    def prizident(self):
        print("Prizident maktabi juda zor maktab")

class Maktab(Ortacha):
    pass

class Ikkinchi_maktab(Maktablar):
    pass

class Tortinchi_maktab(Yomon):
    pass

class Yaxshi(Eng_yaxshi):
    pass

maktab = Maktab()
ikkinchi = Ikkinchi_maktab()
tortinchi = Tortinchi_maktab()
yaxshi = Yaxshi()

ikkinchi.lider()
tortinchi.yaxshimas()
yaxshi.prizident()
maktab.yomonmas()