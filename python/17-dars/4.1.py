# class super metodi (Kvadrat, kub chiqarish)


class Asos:
    
    def __init__(self, bir, ikki):
        self.bir = bir
        self.ikki = ikki
class Kvadrat(Asos):
    
    def __init__(self, bir, ikki):
        super().__init__(bir, ikki)
        
    def natija(self):
        return self.bir*self.ikki
    
class Kub(Asos):
    
    def __init__(self, bir, ikki, uch):
        super().__init__(bir, ikki, )
        self.uch = uch
        
    def natija(self):
        return self.bir*self.ikki*self.uch
class Tortinchi(Kub):
    
    def __init__(self, bir, ikki, uch, tort):
        super().__init__(bir, ikki,uch )
        self.tort = tort
        
    def natija(self):
        return self.bir*self.ikki*self.uch*self.tort
    
class Beshinchi(Tortinchi):
    
    def __init__(self, bir, ikki, uch, tort, besh):
        super().__init__(bir, ikki, uch, tort)
        self.besh = besh        
    def natija(self):
        return self.bir*self.ikki*self.uch*self.tort*self.besh
    
kvadrat = Kvadrat(3, 10)
beshinchi = Beshinchi(5, 5, 5, 5, 5)
print(beshinchi.natija())
print(kvadrat.natija())


    
