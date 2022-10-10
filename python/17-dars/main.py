# class Multilevel inheritance -->

# class Yirtqich:
    
#     def eat(self):
#         print("Bu hayvon yirtqich")
        
# class Ayyor:
    
#     def hiyla(self):
#         print("Bu hayvon ayyor")

# class Bori(Yirtqich):
#     pass

# class Tulki(Ayyor):
#     pass

# class Qush(Yirtqich, Ayyor):
#     pass
    
# bori = Bori()
# tulki = Tulki()
# qush = Qush()

# tulki.hiyla()

# metod overiding (  )

class Animal:
    def walk(self):
        print("Bu yuryapdi")

class Bori(Animal):
    
    def walk(self):
        print("Bu yurish ozgardi")

bori = Bori()
bori.walk()