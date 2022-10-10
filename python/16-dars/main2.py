class Oyinlar():
    
    holati = True

class Counter(Oyinlar):
    
    def qizigi(self):
        print("Ortacha ja zormas")

class Pubg(Counter):
    
    def qiziligi(self):
        print("Juda ham qiziq")
        
class World_of_tanks(Pubg):
    
    def qizigi2(self):
        print("Bu oyin ham juda yaxshi")

class GTA(World_of_tanks):
    
    def qizigi3(self):
        print("YAxshi oyin")

class Maincraft(GTA):
    
    def qizigi4(self):
        print("Yaxshi oyin chidasa boladi")

class Genshin(Maincraft):
    def qizigi5(self):
        print("Chotki oyin")
        
class Dota(Genshin):
    
    def qizigi6(self):
        print("Bu ham zor oyinlardan biri")
        
    
    
        
counter = Counter()
pubg = Pubg()
world = World_of_tanks()
gta = GTA()
maincraft = Maincraft()
genshin = Genshin()
dota = Dota()


print(counter.holati)
pubg.qizigi()
world.qiziligi()
gta.qizigi3()
maincraft.qizigi2()
genshin.qizigi5()
dota.qizigi4()

    