# TEST game
# python dictionary

from pprint import pprint
from turtle import end_fill


def quiz_game ():
    
    tanlanganlar = []
    javoblar = 0
    savol_raqami = 1
    
    for javob in savollar:
        print("--------------------------")
        print(javob)
        for i in variantlar[savol_raqami -1]:
            print(i)
        kirit = input("Quyiga (A, B, C) larni kirit: ").upper()
        tanlanganlar.append(kirit)
        
        javoblar += javob_tekshirish(savollar.get(javob), kirit)
        savol_raqami += 1
        
        natija(javoblar, tanlanganlar)
        


def javob_tekshirish(javob, tanlagan):
    if javob == tanlagan:
        print("To'griiiiii")
        return 1
    else:
        return 0 
            

def natija(javoblar, tanlagan):
    print("------------------")
    print("Natijalar")
    print("------------------")    
    
    print("Javoblar: ", end=" ")
    for i in savollar:
        print(savollar.get(i), end='')
    print()
    
    print("Tanlanganlar: ", end='')
    for i in tanlagan:
        print(i, end=' ')
    print()
    
    natija = int((javoblar/len(savollar))*100)
    print("Sizning natijangiz: " + str(natija) + "%")

def qayta_harakat():
    sorov = input("Qayta harakat qilib korasizmi (Ha, Yo'q): ").upper()
    
    if sorov == "HA":
        return True
    else:
        return False


savollar = {
    "Kim puthonni yaratgan": "A",
    "Qaysi yildi python yaralgan": "C",
    "4 raqami qaysi raqamdan keyin keladi": "D",
    "Yer dumaloqmi": "A"
}



# 2d listlar

variantlar = [
    ["A. Guido Van Rassum", "B. Elon Musk", "C. Bill Gates", "D. Lional Messi"],
    ["A. 2022", "B. 1999", "C. 1989", "D. 1991"],
    ["A. 5", "B. 4", "C. 2", "D. 3"],
    ["A. HA", "B. Yo'q", "C. Bilmadim", "D. To'rtburchak"]
]

quiz_game()

while qayta_harakat():
    quiz_game()
    
print("Oynaganingiz uchun rahmat 😎😎!")